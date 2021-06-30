# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A module that provides functions for handling rapt authentication.

Reauth is a process of obtaining additional authentication (such as password,
security token, etc.) while refreshing OAuth 2.0 credentials for a user.

Credentials that use the Reauth flow must have the reauth scope,
``https://www.googleapis.com/auth/accounts.reauth``.

This module provides a high-level function for executing the Reauth process,
:func:`refresh_grant`, and lower-level helpers for doing the individual
steps of the reauth process.

Those steps are:

1. Obtaining a list of challenges from the reauth server.
2. Running through each challenge and sending the result back to the reauth
   server.
3. Refreshing the access token using the returned rapt token.
"""

import sys

from six.moves import range

from google.auth import exceptions
from google.oauth2 import _client
from google.oauth2 import challenges


_REAUTH_SCOPE = "https://www.googleapis.com/auth/accounts.reauth"
_REAUTH_API = "https://reauth.googleapis.com/v2/sessions"

_REAUTH_NEEDED_ERROR = "invalid_grant"
_REAUTH_NEEDED_ERROR_INVALID_RAPT = "invalid_rapt"
_REAUTH_NEEDED_ERROR_RAPT_REQUIRED = "rapt_required"

_AUTHENTICATED = "AUTHENTICATED"
_CHALLENGE_REQUIRED = "CHALLENGE_REQUIRED"
_CHALLENGE_PENDING = "CHALLENGE_PENDING"


# Override this global variable to set custom max number of rounds of reauth
# challenges should be run.
RUN_CHALLENGE_RETRY_LIMIT = 5


def is_interactive():
    """Check if we are in an interractive environment.

    Override this function with a different logic if you are using this library
    outside a CLI.

    If the rapt token needs refreshing, the user needs to answer the challenges.
    If the user is not in an interractive environment, the challenges can not
    be answered and we just wait for timeout for no reason.

    Returns:
        bool: True if is interactive environment, False otherwise.
    """

    return sys.stdin.isatty()


def _get_challenges(
    request, supported_challenge_types, access_token, requested_scopes=None
):
    """Does initial request to reauth API to get the challenges.

    Args:
        request (google.auth.transport.Request): A callable used to make
            HTTP requests.
        supported_challenge_types (Sequence[str]): list of challenge names
            supported by the manager.
        access_token (str): Access token with reauth scopes.
        requested_scopes (Optional(Sequence[str])): Authorized scopes for the credentials.

    Returns:
        dict: The response from the reauth API.
    """
    body = {"supportedChallengeTypes": supported_challenge_types}
    if requested_scopes:
        body["oauthScopesForDomainPolicyLookup"] = requested_scopes

    return _client._token_endpoint_request(
        request, _REAUTH_API + ":start", body, access_token=access_token, use_json=True
    )


def _send_challenge_result(
    request, session_id, challenge_id, client_input, access_token
):
    """Attempt to refresh access token by sending next challenge result.

    Args:
        request (google.auth.transport.Request): A callable used to make
            HTTP requests.
        session_id (str): session id returned by the initial reauth call.
        challenge_id (str): challenge id returned by the initial reauth call.
        client_input: dict with a challenge-specific client input. For example:
            ``{'credential': password}`` for password challenge.
        access_token (str): Access token with reauth scopes.

    Returns:
        dict: The response from the reauth API.
    """
    body = {
        "sessionId": session_id,
        "challengeId": challenge_id,
        "action": "RESPOND",
        "proposalResponse": client_input,
    }

    return _client._token_endpoint_request(
        request,
        _REAUTH_API + "/{}:continue".format(session_id),
        body,
        access_token=access_token,
        use_json=True,
    )


def _run_next_challenge(msg, request, access_token):
    """Get the next challenge from msg and run it.

    Args:
        msg (dict): Reauth API response body (either from the initial request to
            https://reauth.googleapis.com/v2/sessions:start or from sending the
            previous challenge response to
            https://reauth.googleapis.com/v2/sessions/id:continue)
        request (google.auth.transport.Request): A callable used to make
            HTTP requests.
        access_token (str): reauth access token

    Returns:
        dict: The response from the reauth API.

    Raises:
        google.auth.exceptions.ReauthError: if reauth failed.
    """
    for challenge in msg["challenges"]:
        if challenge["status"] != "READY":
            # Skip non-activated challenges.
            continue
        c = challenges.AVAILABLE_CHALLENGES.get(challenge["challengeType"], None)
        if not c:
            raise exceptions.ReauthFailError(
                "Unsupported challenge type {0}. Supported types: {1}".format(
                    challenge["challengeType"],
                    ",".join(list(challenges.AVAILABLE_CHALLENGES.keys())),
                )
            )
        if not c.is_locally_eligible:
            raise exceptions.ReauthFailError(
                "Challenge {0} is not locally eligible".format(
                    challenge["challengeType"]
                )
            )
        client_input = c.obtain_challenge_input(challenge)
        if not client_input:
            return None
        return _send_challenge_result(
            request,
            msg["sessionId"],
            challenge["challengeId"],
            client_input,
            access_token,
        )
    return None


def _obtain_rapt(request, access_token, requested_scopes):
    """Given an http request method and reauth access token, get rapt token.

    Args:
        request (google.auth.transport.Request): A callable used to make
            HTTP requests.
        access_token (str): reauth access token
        requested_scopes (Sequence[str]): scopes required by the client application

    Returns:
        str: The rapt token.

    Raises:
        google.auth.exceptions.ReauthError: if reauth failed
    """
    msg = _get_challenges(
        request,
        list(challenges.AVAILABLE_CHALLENGES.keys()),
        access_token,
        requested_scopes,
    )

    if msg["status"] == _AUTHENTICATED:
        return msg["encodedProofOfReauthToken"]

    for _ in range(0, RUN_CHALLENGE_RETRY_LIMIT):
        if not (
            msg["status"] == _CHALLENGE_REQUIRED or msg["status"] == _CHALLENGE_PENDING
        ):
            raise exceptions.ReauthFailError(
                "Reauthentication challenge failed due to API error: {}".format(
                    msg["status"]
                )
            )

        if not is_interactive():
            raise exceptions.ReauthFailError(
                "Reauthentication challenge could not be answered because you are not"
                " in an interactive session."
            )

        msg = _run_next_challenge(msg, request, access_token)

        if msg["status"] == _AUTHENTICATED:
            return msg["encodedProofOfReauthToken"]

    # If we got here it means we didn't get authenticated.
    raise exceptions.ReauthFailError("Failed to obtain rapt token.")


def get_rapt_token(
    request, client_id, client_secret, refresh_token, token_uri, scopes=None
):
    """Given an http request method and refresh_token, get rapt token.

    Args:
        request (google.auth.transport.Request): A callable used to make
            HTTP requests.
        client_id (str): client id to get access token for reauth scope.
        client_secret (str): client secret for the client_id
        refresh_token (str): refresh token to refresh access token
        token_uri (str): uri to refresh access token
        scopes (Optional(Sequence[str])): scopes required by the client application

    Returns:
        str: The rapt token.
    Raises:
        google.auth.exceptions.RefreshError: If reauth failed.
    """
    sys.stderr.write("Reauthentication required.\n")

    # Get access token for reauth.
    access_token, _, _, _ = _client.refresh_grant(
        request=request,
        client_id=client_id,
        client_secret=client_secret,
        refresh_token=refresh_token,
        token_uri=token_uri,
        scopes=[_REAUTH_SCOPE],
    )

    # Get rapt token from reauth API.
    rapt_token = _obtain_rapt(request, access_token, requested_scopes=scopes)

    return rapt_token


def refresh_grant(
    request,
    token_uri,
    refresh_token,
    client_id,
    client_secret,
    scopes=None,
    rapt_token=None,
):
    """Implements the reauthentication flow.

    Args:
        request (google.auth.transport.Request): A callable used to make
            HTTP requests.
        token_uri (str): The OAuth 2.0 authorizations server's token endpoint
            URI.
        refresh_token (str): The refresh token to use to get a new access
            token.
        client_id (str): The OAuth 2.0 application's client ID.
        client_secret (str): The Oauth 2.0 appliaction's client secret.
        scopes (Optional(Sequence[str])): Scopes to request. If present, all
            scopes must be authorized for the refresh token. Useful if refresh
            token has a wild card scope (e.g.
            'https://www.googleapis.com/auth/any-api').
        rapt_token (Optional(str)): The rapt token for reauth.

    Returns:
        Tuple[str, Optional[str], Optional[datetime], Mapping[str, str], str]: The
            access token, new refresh token, expiration, the additional data
            returned by the token endpoint, and the rapt token.

    Raises:
        google.auth.exceptions.RefreshError: If the token endpoint returned
            an error.
    """
    body = {
        "grant_type": _client._REFRESH_GRANT_TYPE,
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
    }
    if scopes:
        body["scope"] = " ".join(scopes)
    if rapt_token:
        body["rapt"] = rapt_token

    response_status_ok, response_data = _client._token_endpoint_request_no_throw(
        request, token_uri, body
    )
    if (
        not response_status_ok
        and response_data.get("error") == _REAUTH_NEEDED_ERROR
        and (
            response_data.get("error_subtype") == _REAUTH_NEEDED_ERROR_INVALID_RAPT
            or response_data.get("error_subtype") == _REAUTH_NEEDED_ERROR_RAPT_REQUIRED
        )
    ):
        rapt_token = get_rapt_token(
            request, client_id, client_secret, refresh_token, token_uri, scopes=scopes
        )
        body["rapt"] = rapt_token
        (response_status_ok, response_data) = _client._token_endpoint_request_no_throw(
            request, token_uri, body
        )

    if not response_status_ok:
        _client._handle_error_response(response_data)
    return _client._handle_refresh_grant_response(response_data, refresh_token) + (
        rapt_token,
    )
