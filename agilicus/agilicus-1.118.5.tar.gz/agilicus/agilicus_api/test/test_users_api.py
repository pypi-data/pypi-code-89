"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2021.06.29
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import agilicus_api
from agilicus_api.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_bulk_update_metadata(self):
        """Test case for bulk_update_metadata

        Update a group of user's metadata for the specified org  # noqa: E501
        """
        pass

    def test_create_challenge_method(self):
        """Test case for create_challenge_method

        Create a multi-factor authentication method  # noqa: E501
        """
        pass

    def test_create_service_account(self):
        """Test case for create_service_account

        Create a service account  # noqa: E501
        """
        pass

    def test_create_upstream_user_identity(self):
        """Test case for create_upstream_user_identity

        Create an upstream user identity  # noqa: E501
        """
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a user  # noqa: E501
        """
        pass

    def test_create_user_identity_update(self):
        """Test case for create_user_identity_update

        Update a user's core identity information.  # noqa: E501
        """
        pass

    def test_create_user_metadata(self):
        """Test case for create_user_metadata

        Create a metadata entry for the user  # noqa: E501
        """
        pass

    def test_create_user_request(self):
        """Test case for create_user_request

        Create a request on behalf of the user  # noqa: E501
        """
        pass

    def test_delete_challenge_method(self):
        """Test case for delete_challenge_method

        Delete a user's multi-factor authentication challenge method  # noqa: E501
        """
        pass

    def test_delete_service_account(self):
        """Test case for delete_service_account

        Delete a service account  # noqa: E501
        """
        pass

    def test_delete_upstream_user_identity(self):
        """Test case for delete_upstream_user_identity

        Delete an upstream user identity  # noqa: E501
        """
        pass

    def test_delete_user(self):
        """Test case for delete_user

        Remove a user from an organisation  # noqa: E501
        """
        pass

    def test_delete_user_metadata(self):
        """Test case for delete_user_metadata

        Delete an user metadata entry  # noqa: E501
        """
        pass

    def test_delete_user_request(self):
        """Test case for delete_user_request

        Delete an user request  # noqa: E501
        """
        pass

    def test_get_challenge_method(self):
        """Test case for get_challenge_method

        Get a single challenge method for the given user  # noqa: E501
        """
        pass

    def test_get_service_account(self):
        """Test case for get_service_account

        Get a service account  # noqa: E501
        """
        pass

    def test_get_upstream_user_identity(self):
        """Test case for get_upstream_user_identity

        Get a single upstream user identity  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get a single user  # noqa: E501
        """
        pass

    def test_get_user_metadata(self):
        """Test case for get_user_metadata

        Get a single user metadata entry  # noqa: E501
        """
        pass

    def test_get_user_request(self):
        """Test case for get_user_request

        Get a single user request  # noqa: E501
        """
        pass

    def test_list_access_requests(self):
        """Test case for list_access_requests

        Get a list of access requests  # noqa: E501
        """
        pass

    def test_list_all_resource_permissions(self):
        """Test case for list_all_resource_permissions

        Return all per-resource permissions for a user  # noqa: E501
        """
        pass

    def test_list_all_user_orgs(self):
        """Test case for list_all_user_orgs

        Return all organisations a user has been assigned to  # noqa: E501
        """
        pass

    def test_list_all_user_roles(self):
        """Test case for list_all_user_roles

        Return all roles for a user  # noqa: E501
        """
        pass

    def test_list_challenge_methods(self):
        """Test case for list_challenge_methods

        Get all of a user's multi-factor authentication challenge method configuration  # noqa: E501
        """
        pass

    def test_list_combined_user_details(self):
        """Test case for list_combined_user_details

        Get all combined details about users  # noqa: E501
        """
        pass

    def test_list_org_user_roles(self):
        """Test case for list_org_user_roles

        Get all org user roles  # noqa: E501
        """
        pass

    def test_list_service_accounts(self):
        """Test case for list_service_accounts

        List service accounts  # noqa: E501
        """
        pass

    def test_list_upstream_user_identities(self):
        """Test case for list_upstream_user_identities

        Get all of a user's upstream user identities  # noqa: E501
        """
        pass

    def test_list_user_application_access_info(self):
        """Test case for list_user_application_access_info

        Query various users' application access information  # noqa: E501
        """
        pass

    def test_list_user_file_share_access_info(self):
        """Test case for list_user_file_share_access_info

        Query various users' file share access information  # noqa: E501
        """
        pass

    def test_list_user_guids(self):
        """Test case for list_user_guids

        Get a list of all user GUIDs  # noqa: E501
        """
        pass

    def test_list_user_metadata(self):
        """Test case for list_user_metadata

        Get a list of user metadata entries  # noqa: E501
        """
        pass

    def test_list_user_permissions(self):
        """Test case for list_user_permissions

        Return the user's host permissions  # noqa: E501
        """
        pass

    def test_list_user_requests(self):
        """Test case for list_user_requests

        Get a list of user requests  # noqa: E501
        """
        pass

    def test_list_user_resource_access_info(self):
        """Test case for list_user_resource_access_info

        Query various users' resource access information  # noqa: E501
        """
        pass

    def test_list_users(self):
        """Test case for list_users

        Get all users  # noqa: E501
        """
        pass

    def test_replace_challenge_method(self):
        """Test case for replace_challenge_method

        Update a user's multi-factor authentication challenge method  # noqa: E501
        """
        pass

    def test_replace_service_account(self):
        """Test case for replace_service_account

        Update a service account  # noqa: E501
        """
        pass

    def test_replace_upstream_user_identity(self):
        """Test case for replace_upstream_user_identity

        Update an upstream user identity  # noqa: E501
        """
        pass

    def test_replace_user(self):
        """Test case for replace_user

        Create or update a user  # noqa: E501
        """
        pass

    def test_replace_user_metadata(self):
        """Test case for replace_user_metadata

        Update an user metadata entry.  # noqa: E501
        """
        pass

    def test_replace_user_request(self):
        """Test case for replace_user_request

        Update an user request. Note this method ignores the state parameter.  # noqa: E501
        """
        pass

    def test_replace_user_role(self):
        """Test case for replace_user_role

        Create or update a user role  # noqa: E501
        """
        pass

    def test_reset_user_mfa_challenge_methods(self):
        """Test case for reset_user_mfa_challenge_methods

        Resets a user's multi-factor authentication method  # noqa: E501
        """
        pass

    def test_update_user_request(self):
        """Test case for update_user_request

        Uses the state parameter in the body to apply the action to the request  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
