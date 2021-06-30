# flake8: noqa

"""
    Engines API

    Allow clients to fetch Analytics through APIs.  # noqa: E501

    The version of the OpenAPI document: v3:[pa,spar,vault,pub,quant,fi,axp,afi,npo,bpm,fpo,others],v1:[fiab]
    Contact: analytics.api.support@factset.com
    Generated by: https://openapi-generator.tech
"""


__version__ = "5.0.1"

# import ApiClient
from fds.analyticsapi.engines.api_client import ApiClient

# import Configuration
from fds.analyticsapi.engines.configuration import Configuration

# import exceptions
from fds.analyticsapi.engines.exceptions import OpenApiException
from fds.analyticsapi.engines.exceptions import ApiAttributeError
from fds.analyticsapi.engines.exceptions import ApiTypeError
from fds.analyticsapi.engines.exceptions import ApiValueError
from fds.analyticsapi.engines.exceptions import ApiKeyError
from fds.analyticsapi.engines.exceptions import ApiException
