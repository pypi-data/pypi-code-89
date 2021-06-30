"""
    Agilicus API

    Agilicus is API-first. Modern software is controlled by other software, is open, is available for you to use the way you want, securely, simply.  A rendered, online viewable and usable version of this specification is available at [api](https://www.agilicus.com/api). You may try the API inline directly in the web page. To do so, first obtain an Authentication Token (the simplest way is to install the Python SDK, and then run `agilicus-cli --issuer https://MYISSUER get-token`). You will need an org-id for most calls (and can obtain from `agilicus-cli --issuer https://MYISSUER list-orgs`). The `MYISSUER` will typically be `auth.MYDOMAIN`, and you will see it as you sign-in to the administrative UI.  This API releases on Bearer-Token authentication. To obtain a valid bearer token you will need to Authenticate to an Issuer with OpenID Connect (a superset of OAUTH2).  Your \"issuer\" will look like https://auth.MYDOMAIN. For example, when you signed-up, if you said \"use my own domain name\" and assigned a CNAME of cloud.example.com, then your issuer would be https://auth.cloud.example.com.  If you selected \"use an Agilicus supplied domain name\", your issuer would look like https://auth.myorg.agilicus.cloud.  For test purposes you can use our [Python SDK](https://pypi.org/project/agilicus/) and run `agilicus-cli --issuer https://auth.MYDOMAIN get-token`.  This API may be used in any language runtime that supports OpenAPI 3.0, or, you may use our [Python SDK](https://pypi.org/project/agilicus/), our [Typescript SDK](https://www.npmjs.com/package/@agilicus/angular), or our [Golang SDK](https://git.agilicus.com/pub/sdk-go).  100% of the activities in our system our API-driven, from our web-admin, through our progressive web applications, to all internals: there is nothing that is not accessible.  For more information, see [developer resources](https://www.agilicus.com/developer).   # noqa: E501

    The version of the OpenAPI document: 2021.06.29
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from agilicus_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from agilicus_api.exceptions import ApiAttributeError



class AuthAudits(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @property
    def user_id(self):
       return self.get("user_id")

    @user_id.setter
    def user_id(self, new_value):
       self.user_id = new_value

    @property
    def upstream_user_id(self):
       return self.get("upstream_user_id")

    @upstream_user_id.setter
    def upstream_user_id(self, new_value):
       self.upstream_user_id = new_value

    @property
    def org_id(self):
       return self.get("org_id")

    @org_id.setter
    def org_id(self, new_value):
       self.org_id = new_value

    @property
    def org_name(self):
       return self.get("org_name")

    @org_name.setter
    def org_name(self, new_value):
       self.org_name = new_value

    @property
    def time(self):
       return self.get("time")

    @time.setter
    def time(self, new_value):
       self.time = new_value

    @property
    def event(self):
       return self.get("event")

    @event.setter
    def event(self, new_value):
       self.event = new_value

    @property
    def source_ip(self):
       return self.get("source_ip")

    @source_ip.setter
    def source_ip(self, new_value):
       self.source_ip = new_value

    @property
    def token_id(self):
       return self.get("token_id")

    @token_id.setter
    def token_id(self, new_value):
       self.token_id = new_value

    @property
    def trace_id(self):
       return self.get("trace_id")

    @trace_id.setter
    def trace_id(self, new_value):
       self.trace_id = new_value

    @property
    def session(self):
       return self.get("session")

    @session.setter
    def session(self, new_value):
       self.session = new_value

    @property
    def issuer(self):
       return self.get("issuer")

    @issuer.setter
    def issuer(self, new_value):
       self.issuer = new_value

    @property
    def client_id(self):
       return self.get("client_id")

    @client_id.setter
    def client_id(self, new_value):
       self.client_id = new_value

    @property
    def application_name(self):
       return self.get("application_name")

    @application_name.setter
    def application_name(self, new_value):
       self.application_name = new_value

    @property
    def login_org_id(self):
       return self.get("login_org_id")

    @login_org_id.setter
    def login_org_id(self, new_value):
       self.login_org_id = new_value

    @property
    def login_org_name(self):
       return self.get("login_org_name")

    @login_org_name.setter
    def login_org_name(self, new_value):
       self.login_org_name = new_value

    @property
    def upstream_idp(self):
       return self.get("upstream_idp")

    @upstream_idp.setter
    def upstream_idp(self, new_value):
       self.upstream_idp = new_value

    @property
    def stage(self):
       return self.get("stage")

    @stage.setter
    def stage(self, new_value):
       self.stage = new_value

    @property
    def user_agent(self):
       return self.get("user_agent")

    @user_agent.setter
    def user_agent(self, new_value):
       self.user_agent = new_value

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'user_id': (str,),  # noqa: E501
            'upstream_user_id': (str,),  # noqa: E501
            'org_id': (str,),  # noqa: E501
            'org_name': (str,),  # noqa: E501
            'time': (datetime,),  # noqa: E501
            'event': (str,),  # noqa: E501
            'source_ip': (str,),  # noqa: E501
            'token_id': (str,),  # noqa: E501
            'trace_id': (str,),  # noqa: E501
            'session': (str,),  # noqa: E501
            'issuer': (str,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'application_name': (str,),  # noqa: E501
            'login_org_id': (str,),  # noqa: E501
            'login_org_name': (str,),  # noqa: E501
            'upstream_idp': (str,),  # noqa: E501
            'stage': (str,),  # noqa: E501
            'user_agent': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'user_id': 'user_id',  # noqa: E501
        'upstream_user_id': 'upstream_user_id',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'org_name': 'org_name',  # noqa: E501
        'time': 'time',  # noqa: E501
        'event': 'event',  # noqa: E501
        'source_ip': 'source_ip',  # noqa: E501
        'token_id': 'token_id',  # noqa: E501
        'trace_id': 'trace_id',  # noqa: E501
        'session': 'session',  # noqa: E501
        'issuer': 'issuer',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
        'application_name': 'application_name',  # noqa: E501
        'login_org_id': 'login_org_id',  # noqa: E501
        'login_org_name': 'login_org_name',  # noqa: E501
        'upstream_idp': 'upstream_idp',  # noqa: E501
        'stage': 'stage',  # noqa: E501
        'user_agent': 'user_agent',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AuthAudits - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            user_id (str): The system-local id of the user performing the action.. [optional]  # noqa: E501
            upstream_user_id (str): The id of the user in the upstream system, if available.. [optional]  # noqa: E501
            org_id (str): The id of the organisation of the issuer against which the user is authenticating. . [optional]  # noqa: E501
            org_name (str): The name of the organisation of the issuer against which the user is authenticating. . [optional]  # noqa: E501
            time (datetime): the time at which the record was generated.. [optional]  # noqa: E501
            event (str): The event which generated the record. The meaning of the event depends on the stage where it occured. . [optional]  # noqa: E501
            source_ip (str): The IP address of the host initiating the action. [optional]  # noqa: E501
            token_id (str): The id of the token issued or reissued as part of the authentication.. [optional]  # noqa: E501
            trace_id (str): A correlation ID associated with requests related to this event. [optional]  # noqa: E501
            session (str): The session associated with tokens related to this event. This can be used to tie the actions undertaking by requests bearing tokens with the same session back to the authentication events which created the tokens. . [optional]  # noqa: E501
            issuer (str): The issuer the user logged in to.. [optional]  # noqa: E501
            client_id (str): The client id of the web application, client, etc. that the user is logging in with. Note that this is not the id of the `IssuerClient`, but rather the id presented to the authentication system to identify that client. This corresponds to `name` in the `IssuerClient`. . [optional]  # noqa: E501
            application_name (str): The name of the application within the system the user is logging in to.. [optional]  # noqa: E501
            login_org_id (str): The id of the organisation that the user is logging in to. Note that this is disctinct from the `org_id` field, which is tied to the issuer. This id is tied to the application. . [optional]  # noqa: E501
            login_org_name (str): The name of the organisation that the user is logging in to. This corresponds to `login_org_id`. . [optional]  # noqa: E501
            upstream_idp (str): The name of the identity provider proving the identity of the user. . [optional]  # noqa: E501
            stage (str): The stage of the login process. This identifies where in the pipeline the event was generated. . [optional]  # noqa: E501
            user_agent (str): The user agent of the client used to perform the login. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    def __python_set(val):
        return set(val)
 
    required_properties = __python_set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """AuthAudits - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            user_id (str): The system-local id of the user performing the action.. [optional]  # noqa: E501
            upstream_user_id (str): The id of the user in the upstream system, if available.. [optional]  # noqa: E501
            org_id (str): The id of the organisation of the issuer against which the user is authenticating. . [optional]  # noqa: E501
            org_name (str): The name of the organisation of the issuer against which the user is authenticating. . [optional]  # noqa: E501
            time (datetime): the time at which the record was generated.. [optional]  # noqa: E501
            event (str): The event which generated the record. The meaning of the event depends on the stage where it occured. . [optional]  # noqa: E501
            source_ip (str): The IP address of the host initiating the action. [optional]  # noqa: E501
            token_id (str): The id of the token issued or reissued as part of the authentication.. [optional]  # noqa: E501
            trace_id (str): A correlation ID associated with requests related to this event. [optional]  # noqa: E501
            session (str): The session associated with tokens related to this event. This can be used to tie the actions undertaking by requests bearing tokens with the same session back to the authentication events which created the tokens. . [optional]  # noqa: E501
            issuer (str): The issuer the user logged in to.. [optional]  # noqa: E501
            client_id (str): The client id of the web application, client, etc. that the user is logging in with. Note that this is not the id of the `IssuerClient`, but rather the id presented to the authentication system to identify that client. This corresponds to `name` in the `IssuerClient`. . [optional]  # noqa: E501
            application_name (str): The name of the application within the system the user is logging in to.. [optional]  # noqa: E501
            login_org_id (str): The id of the organisation that the user is logging in to. Note that this is disctinct from the `org_id` field, which is tied to the issuer. This id is tied to the application. . [optional]  # noqa: E501
            login_org_name (str): The name of the organisation that the user is logging in to. This corresponds to `login_org_id`. . [optional]  # noqa: E501
            upstream_idp (str): The name of the identity provider proving the identity of the user. . [optional]  # noqa: E501
            stage (str): The stage of the login process. This identifies where in the pipeline the event was generated. . [optional]  # noqa: E501
            user_agent (str): The user agent of the client used to perform the login. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

