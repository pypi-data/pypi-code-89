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


def lazy_import():
    from agilicus_api.model.file_name import FileName
    from agilicus_api.model.file_visibility import FileVisibility
    from agilicus_api.model.storage_region import StorageRegion
    globals()['FileName'] = FileName
    globals()['FileVisibility'] = FileVisibility
    globals()['StorageRegion'] = StorageRegion


class File(ModelNormal):
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
    def id(self):
       return self.get("id")

    @id.setter
    def id(self, new_value):
       self.id = new_value

    @property
    def name(self):
       return self.get("name")

    @name.setter
    def name(self, new_value):
       self.name = new_value

    @property
    def tag(self):
       return self.get("tag")

    @tag.setter
    def tag(self, new_value):
       self.tag = new_value

    @property
    def label(self):
       return self.get("label")

    @label.setter
    def label(self, new_value):
       self.label = new_value

    @property
    def size(self):
       return self.get("size")

    @size.setter
    def size(self, new_value):
       self.size = new_value

    @property
    def visibility(self):
       return self.get("visibility")

    @visibility.setter
    def visibility(self, new_value):
       self.visibility = new_value

    @property
    def public_url(self):
       return self.get("public_url")

    @public_url.setter
    def public_url(self, new_value):
       self.public_url = new_value

    @property
    def region(self):
       return self.get("region")

    @region.setter
    def region(self, new_value):
       self.region = new_value

    @property
    def lock(self):
       return self.get("lock")

    @lock.setter
    def lock(self, new_value):
       self.lock = new_value

    @property
    def storage_path(self):
       return self.get("storage_path")

    @storage_path.setter
    def storage_path(self, new_value):
       self.storage_path = new_value

    @property
    def md5_hash(self):
       return self.get("md5_hash")

    @md5_hash.setter
    def md5_hash(self, new_value):
       self.md5_hash = new_value

    @property
    def last_accessed(self):
       return self.get("last_accessed")

    @last_accessed.setter
    def last_accessed(self, new_value):
       self.last_accessed = new_value

    @property
    def created(self):
       return self.get("created")

    @created.setter
    def created(self, new_value):
       self.created = new_value

    @property
    def updated(self):
       return self.get("updated")

    @updated.setter
    def updated(self, new_value):
       self.updated = new_value

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
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
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'name': (FileName,),  # noqa: E501
            'tag': (str,),  # noqa: E501
            'label': (str,),  # noqa: E501
            'size': (int,),  # noqa: E501
            'visibility': (FileVisibility,),  # noqa: E501
            'public_url': (str,),  # noqa: E501
            'region': (StorageRegion,),  # noqa: E501
            'lock': (bool,),  # noqa: E501
            'storage_path': (str,),  # noqa: E501
            'md5_hash': (str,),  # noqa: E501
            'last_accessed': (datetime,),  # noqa: E501
            'created': (datetime,),  # noqa: E501
            'updated': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None



    attribute_map = {
        'id': 'id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'tag': 'tag',  # noqa: E501
        'label': 'label',  # noqa: E501
        'size': 'size',  # noqa: E501
        'visibility': 'visibility',  # noqa: E501
        'public_url': 'public_url',  # noqa: E501
        'region': 'region',  # noqa: E501
        'lock': 'lock',  # noqa: E501
        'storage_path': 'storage_path',  # noqa: E501
        'md5_hash': 'md5_hash',  # noqa: E501
        'last_accessed': 'last_accessed',  # noqa: E501
        'created': 'created',  # noqa: E501
        'updated': 'updated',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'size',  # noqa: E501
        'public_url',  # noqa: E501
        'storage_path',  # noqa: E501
        'md5_hash',  # noqa: E501
        'last_accessed',  # noqa: E501
        'created',  # noqa: E501
        'updated',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """File - a model defined in OpenAPI

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
            id (str): Unique identifier. [optional]  # noqa: E501
            name (FileName): [optional]  # noqa: E501
            tag (str): A file tag. [optional]  # noqa: E501
            label (str): A file label. [optional]  # noqa: E501
            size (int): Size in bytes of the file. [optional]  # noqa: E501
            visibility (FileVisibility): [optional]  # noqa: E501
            public_url (str): The location of the file on the internet. If present, this file can be downloaded by requesting this URI. If the file is publically visible, then no credentials need be provided. . [optional]  # noqa: E501
            region (StorageRegion): [optional]  # noqa: E501
            lock (bool): Locking prevents the deletion or modification of the file. [optional]  # noqa: E501
            storage_path (str): storage path. [optional]  # noqa: E501
            md5_hash (str): MD5 Hash of file in base64. [optional]  # noqa: E501
            last_accessed (datetime): Time object was last accessed. [optional]  # noqa: E501
            created (datetime): Creation time. [optional]  # noqa: E501
            updated (datetime): Update time. [optional]  # noqa: E501
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
        """File - a model defined in OpenAPI

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
            id (str): Unique identifier. [optional]  # noqa: E501
            name (FileName): [optional]  # noqa: E501
            tag (str): A file tag. [optional]  # noqa: E501
            label (str): A file label. [optional]  # noqa: E501
            size (int): Size in bytes of the file. [optional]  # noqa: E501
            visibility (FileVisibility): [optional]  # noqa: E501
            public_url (str): The location of the file on the internet. If present, this file can be downloaded by requesting this URI. If the file is publically visible, then no credentials need be provided. . [optional]  # noqa: E501
            region (StorageRegion): [optional]  # noqa: E501
            lock (bool): Locking prevents the deletion or modification of the file. [optional]  # noqa: E501
            storage_path (str): storage path. [optional]  # noqa: E501
            md5_hash (str): MD5 Hash of file in base64. [optional]  # noqa: E501
            last_accessed (datetime): Time object was last accessed. [optional]  # noqa: E501
            created (datetime): Creation time. [optional]  # noqa: E501
            updated (datetime): Update time. [optional]  # noqa: E501
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

