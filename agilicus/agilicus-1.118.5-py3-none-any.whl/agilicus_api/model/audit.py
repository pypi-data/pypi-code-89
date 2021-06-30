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



class Audit(ModelNormal):
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
    def target_resource_type(self):
       return self.get("target_resource_type")

    @target_resource_type.setter
    def target_resource_type(self, new_value):
       self.target_resource_type = new_value

    @property
    def api_name(self):
       return self.get("api_name")

    @api_name.setter
    def api_name(self, new_value):
       self.api_name = new_value

    @property
    def org_id(self):
       return self.get("org_id")

    @org_id.setter
    def org_id(self, new_value):
       self.org_id = new_value

    @property
    def time(self):
       return self.get("time")

    @time.setter
    def time(self, new_value):
       self.time = new_value

    @property
    def action(self):
       return self.get("action")

    @action.setter
    def action(self, new_value):
       self.action = new_value

    @property
    def source_ip(self):
       return self.get("source_ip")

    @source_ip.setter
    def source_ip(self, new_value):
       self.source_ip = new_value

    @property
    def target_id(self):
       return self.get("target_id")

    @target_id.setter
    def target_id(self, new_value):
       self.target_id = new_value

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
    def secondary_id(self):
       return self.get("secondary_id")

    @secondary_id.setter
    def secondary_id(self, new_value):
       self.secondary_id = new_value

    @property
    def tertiary_id(self):
       return self.get("tertiary_id")

    @tertiary_id.setter
    def tertiary_id(self, new_value):
       self.tertiary_id = new_value

    @property
    def parent_id(self):
       return self.get("parent_id")

    @parent_id.setter
    def parent_id(self, new_value):
       self.parent_id = new_value

    @property
    def grandparent_id(self):
       return self.get("grandparent_id")

    @grandparent_id.setter
    def grandparent_id(self, new_value):
       self.grandparent_id = new_value

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
            'target_resource_type': (str,),  # noqa: E501
            'api_name': (str,),  # noqa: E501
            'org_id': (str,),  # noqa: E501
            'time': (datetime,),  # noqa: E501
            'action': (str,),  # noqa: E501
            'source_ip': (str,),  # noqa: E501
            'target_id': (str,),  # noqa: E501
            'token_id': (str,),  # noqa: E501
            'trace_id': (str,),  # noqa: E501
            'session': (str,),  # noqa: E501
            'secondary_id': (str,),  # noqa: E501
            'tertiary_id': (str,),  # noqa: E501
            'parent_id': (str,),  # noqa: E501
            'grandparent_id': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'user_id': 'user_id',  # noqa: E501
        'target_resource_type': 'target_resource_type',  # noqa: E501
        'api_name': 'api_name',  # noqa: E501
        'org_id': 'org_id',  # noqa: E501
        'time': 'time',  # noqa: E501
        'action': 'action',  # noqa: E501
        'source_ip': 'source_ip',  # noqa: E501
        'target_id': 'target_id',  # noqa: E501
        'token_id': 'token_id',  # noqa: E501
        'trace_id': 'trace_id',  # noqa: E501
        'session': 'session',  # noqa: E501
        'secondary_id': 'secondary_id',  # noqa: E501
        'tertiary_id': 'tertiary_id',  # noqa: E501
        'parent_id': 'parent_id',  # noqa: E501
        'grandparent_id': 'grandparent_id',  # noqa: E501
    }

    read_only_vars = {
        'user_id',  # noqa: E501
        'target_resource_type',  # noqa: E501
        'api_name',  # noqa: E501
        'org_id',  # noqa: E501
        'time',  # noqa: E501
        'source_ip',  # noqa: E501
        'target_id',  # noqa: E501
        'token_id',  # noqa: E501
        'trace_id',  # noqa: E501
        'session',  # noqa: E501
        'secondary_id',  # noqa: E501
        'tertiary_id',  # noqa: E501
        'parent_id',  # noqa: E501
        'grandparent_id',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Audit - a model defined in OpenAPI

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
            user_id (str): The id of the user performing the action. [optional]  # noqa: E501
            target_resource_type (str): The name of the resource type which was affected by the event which generated this record. The `target_id` field will uniquely identify, if possible, the record within the resource type. . [optional]  # noqa: E501
            api_name (str): The name of the API which generated the event. This will typically be a single value for many different target_resource_types. . [optional]  # noqa: E501
            org_id (str): The organization of the user performing the action. [optional]  # noqa: E501
            time (datetime): the time at which the log was generated. [optional]  # noqa: E501
            action (str): The type of action performed on the target. [optional]  # noqa: E501
            source_ip (str): The IP address of the host initating the action. [optional]  # noqa: E501
            target_id (str): The id of the resource affected by the action. [optional]  # noqa: E501
            token_id (str): The id of the bearer token used to authenticate when performing the action. [optional]  # noqa: E501
            trace_id (str): A correlation ID associated with requests related to this action. [optional]  # noqa: E501
            session (str): The session associated with this action. Sessions typically span multiple tokens. . [optional]  # noqa: E501
            secondary_id (str): The secondary id of the resource affected by the action if one exists. This can occur if the resource's primary key is a composite key. APIs whose resources are not referenced by a GUID in the path make use of these fields for example the replace_user_role endpoint uses the user_id, and application to identify a resource. . [optional]  # noqa: E501
            tertiary_id (str): The tertiary id of the resource affected by the action if one exists. This can occur if the resource's primary key is a composite key. . [optional]  # noqa: E501
            parent_id (str): The id of the parent resource for the resource affected by the action. An example of this is the path /v1/collection/2jkdcmwB97jh3kiglnz/subcollection/idabc123. The resource belongs to the `subcollection` which falls under the parent in this case `collection`. As a resulti idabc123 is the target_id, 2jkdCmwB9u7Jh3KIglNZ is the parent ID . [optional]  # noqa: E501
            grandparent_id (str): The id of the grandparent resource for the resource affected by the action. An example of this is the path /v1/collection/2jkdcmwB97jh3kiglnz/subcollection/2334115135/subsubcolletion/aaabbbccc Similar to the parent id example  aaabbbccc is the target_id, 2334115135 is the parent ID and 2jkdcmwB97jh3kiglnz is the grandparent_id . [optional]  # noqa: E501
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
        """Audit - a model defined in OpenAPI

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
            user_id (str): The id of the user performing the action. [optional]  # noqa: E501
            target_resource_type (str): The name of the resource type which was affected by the event which generated this record. The `target_id` field will uniquely identify, if possible, the record within the resource type. . [optional]  # noqa: E501
            api_name (str): The name of the API which generated the event. This will typically be a single value for many different target_resource_types. . [optional]  # noqa: E501
            org_id (str): The organization of the user performing the action. [optional]  # noqa: E501
            time (datetime): the time at which the log was generated. [optional]  # noqa: E501
            action (str): The type of action performed on the target. [optional]  # noqa: E501
            source_ip (str): The IP address of the host initating the action. [optional]  # noqa: E501
            target_id (str): The id of the resource affected by the action. [optional]  # noqa: E501
            token_id (str): The id of the bearer token used to authenticate when performing the action. [optional]  # noqa: E501
            trace_id (str): A correlation ID associated with requests related to this action. [optional]  # noqa: E501
            session (str): The session associated with this action. Sessions typically span multiple tokens. . [optional]  # noqa: E501
            secondary_id (str): The secondary id of the resource affected by the action if one exists. This can occur if the resource's primary key is a composite key. APIs whose resources are not referenced by a GUID in the path make use of these fields for example the replace_user_role endpoint uses the user_id, and application to identify a resource. . [optional]  # noqa: E501
            tertiary_id (str): The tertiary id of the resource affected by the action if one exists. This can occur if the resource's primary key is a composite key. . [optional]  # noqa: E501
            parent_id (str): The id of the parent resource for the resource affected by the action. An example of this is the path /v1/collection/2jkdcmwB97jh3kiglnz/subcollection/idabc123. The resource belongs to the `subcollection` which falls under the parent in this case `collection`. As a resulti idabc123 is the target_id, 2jkdCmwB9u7Jh3KIglNZ is the parent ID . [optional]  # noqa: E501
            grandparent_id (str): The id of the grandparent resource for the resource affected by the action. An example of this is the path /v1/collection/2jkdcmwB97jh3kiglnz/subcollection/2334115135/subsubcolletion/aaabbbccc Similar to the parent id example  aaabbbccc is the target_id, 2334115135 is the parent ID and 2jkdcmwB97jh3kiglnz is the grandparent_id . [optional]  # noqa: E501
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

