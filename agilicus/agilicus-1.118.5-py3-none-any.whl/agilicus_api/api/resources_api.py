"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2021.06.29
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from agilicus_api.api_client import ApiClient, Endpoint as _Endpoint
from agilicus_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from agilicus_api.model.list_resources_response import ListResourcesResponse


class ResourcesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __list_resources(
            self,
            **kwargs
        ):
            """List all Resources  # noqa: E501

            List all Resources matching the provided query parameters. Perform keyset pagination by setting the page_at_id parameter to the id for the next page to fetch. Set it to `\"\"` to start from the beginning.   # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_resources(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                limit (int): limit the number of rows in the response. [optional] if omitted the server will use the default value of 500
                org_id (str): Organisation Unique identifier. [optional]
                resource_type (str): The type of resource to query for. [optional]
                name_slug (str): The slug of the resource to query for. [optional]
                name (str): The name of the resource to query for. [optional]
                resource_id (str): The id of the resource to query for. [optional]
                page_at_id (str): Pagination based query with the id as the key. To get the initial entries supply an empty string. On subsequent requests, supply the `page_at_id` field from the list response. . [optional]
                org_ids ([str]): The list of org ids to search for. Each org will be searched for independently.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListResourcesResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            return self.call_with_http_info(**kwargs)

        if self.list_resources is None:
            self.list_resources = _Endpoint(
                settings={
                    'response_type': (ListResourcesResponse,),
                    'auth': [
                        'token-valid'
                    ],
                    'endpoint_path': '/v1/resources',
                    'operation_id': 'list_resources',
                    'http_method': 'GET',
                    'servers': None,
                },
                params_map={
                    'all': [
                        'limit',
                        'org_id',
                        'resource_type',
                        'name_slug',
                        'name',
                        'resource_id',
                        'page_at_id',
                        'org_ids',
                    ],
                    'required': [],
                    'nullable': [
                    ],
                    'enum': [
                    ],
                    'validation': [
                        'limit',
                        'name',
                    ]
                },
                root_map={
                    'validations': {
                        ('limit',): {

                            'inclusive_maximum': 500,
                            'inclusive_minimum': 1,
                        },
                        ('name',): {
                            'max_length': 100,
                            'regex': {
                                'pattern': r'^[a-zA-Z0-9-_.:]+$',  # noqa: E501
                            },
                        },
                    },
                    'allowed_values': {
                    },
                    'openapi_types': {
                        'limit':
                            (int,),
                        'org_id':
                            (str,),
                        'resource_type':
                            (str,),
                        'name_slug':
                            (str,),
                        'name':
                            (str,),
                        'resource_id':
                            (str,),
                        'page_at_id':
                            (str,),
                        'org_ids':
                            ([str],),
                    },
                    'attribute_map': {
                        'limit': 'limit',
                        'org_id': 'org_id',
                        'resource_type': 'resource_type',
                        'name_slug': 'name_slug',
                        'name': 'name',
                        'resource_id': 'resource_id',
                        'page_at_id': 'page_at_id',
                        'org_ids': 'org_ids',
                    },
                    'location_map': {
                        'limit': 'query',
                        'org_id': 'query',
                        'resource_type': 'query',
                        'name_slug': 'query',
                        'name': 'query',
                        'resource_id': 'query',
                        'page_at_id': 'query',
                        'org_ids': 'query',
                    },
                    'collection_format_map': {
                        'org_ids': 'multi',
                    }
                },
                headers_map={
                    'accept': [
                        'application/json'
                    ],
                    'content_type': [],
                },
                api_client=api_client,
                callable=__list_resources
            )

    list_resources = None 
