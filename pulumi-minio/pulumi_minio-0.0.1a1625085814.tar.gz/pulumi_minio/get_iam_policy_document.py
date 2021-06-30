# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetIamPolicyDocumentResult',
    'AwaitableGetIamPolicyDocumentResult',
    'get_iam_policy_document',
]

@pulumi.output_type
class GetIamPolicyDocumentResult:
    """
    A collection of values returned by getIamPolicyDocument.
    """
    def __init__(__self__, id=None, json=None, override_json=None, policy_id=None, source_json=None, statements=None, version=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if json and not isinstance(json, str):
            raise TypeError("Expected argument 'json' to be a str")
        pulumi.set(__self__, "json", json)
        if override_json and not isinstance(override_json, str):
            raise TypeError("Expected argument 'override_json' to be a str")
        pulumi.set(__self__, "override_json", override_json)
        if policy_id and not isinstance(policy_id, str):
            raise TypeError("Expected argument 'policy_id' to be a str")
        pulumi.set(__self__, "policy_id", policy_id)
        if source_json and not isinstance(source_json, str):
            raise TypeError("Expected argument 'source_json' to be a str")
        pulumi.set(__self__, "source_json", source_json)
        if statements and not isinstance(statements, list):
            raise TypeError("Expected argument 'statements' to be a list")
        pulumi.set(__self__, "statements", statements)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def json(self) -> str:
        return pulumi.get(self, "json")

    @property
    @pulumi.getter(name="overrideJson")
    def override_json(self) -> Optional[str]:
        return pulumi.get(self, "override_json")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[str]:
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter(name="sourceJson")
    def source_json(self) -> Optional[str]:
        return pulumi.get(self, "source_json")

    @property
    @pulumi.getter
    def statements(self) -> Optional[Sequence['outputs.GetIamPolicyDocumentStatementResult']]:
        return pulumi.get(self, "statements")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")


class AwaitableGetIamPolicyDocumentResult(GetIamPolicyDocumentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIamPolicyDocumentResult(
            id=self.id,
            json=self.json,
            override_json=self.override_json,
            policy_id=self.policy_id,
            source_json=self.source_json,
            statements=self.statements,
            version=self.version)


def get_iam_policy_document(override_json: Optional[str] = None,
                            policy_id: Optional[str] = None,
                            source_json: Optional[str] = None,
                            statements: Optional[Sequence[pulumi.InputType['GetIamPolicyDocumentStatementArgs']]] = None,
                            version: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIamPolicyDocumentResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['overrideJson'] = override_json
    __args__['policyId'] = policy_id
    __args__['sourceJson'] = source_json
    __args__['statements'] = statements
    __args__['version'] = version
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('minio:index/getIamPolicyDocument:getIamPolicyDocument', __args__, opts=opts, typ=GetIamPolicyDocumentResult).value

    return AwaitableGetIamPolicyDocumentResult(
        id=__ret__.id,
        json=__ret__.json,
        override_json=__ret__.override_json,
        policy_id=__ret__.policy_id,
        source_json=__ret__.source_json,
        statements=__ret__.statements,
        version=__ret__.version)
