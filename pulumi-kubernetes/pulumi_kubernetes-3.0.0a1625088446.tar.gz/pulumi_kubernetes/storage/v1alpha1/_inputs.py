# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ... import core as _core
from ... import meta as _meta

__all__ = [
    'CSIStorageCapacityArgs',
    'VolumeAttachmentArgs',
    'VolumeAttachmentSourceArgs',
    'VolumeAttachmentSpecArgs',
    'VolumeAttachmentStatusArgs',
    'VolumeErrorArgs',
]

@pulumi.input_type
class CSIStorageCapacityArgs:
    def __init__(__self__, *,
                 storage_class_name: pulumi.Input[str],
                 api_version: Optional[pulumi.Input[str]] = None,
                 capacity: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 maximum_volume_size: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']] = None,
                 node_topology: Optional[pulumi.Input['_meta.v1.LabelSelectorArgs']] = None):
        """
        CSIStorageCapacity stores the result of one CSI GetCapacity call. For a given StorageClass, this describes the available capacity in a particular topology segment.  This can be used when considering where to instantiate new PersistentVolumes.

        For example this can express things like: - StorageClass "standard" has "1234 GiB" available in "topology.kubernetes.io/zone=us-east1" - StorageClass "localssd" has "10 GiB" available in "kubernetes.io/hostname=knode-abc123"

        The following three cases all imply that no capacity is available for a certain combination: - no object exists with suitable topology and storage class name - such an object exists, but the capacity is unset - such an object exists, but the capacity is zero

        The producer of these objects can decide which approach is more suitable.

        They are consumed by the kube-scheduler if the CSIStorageCapacity beta feature gate is enabled there and a CSI driver opts into capacity-aware scheduling with CSIDriver.StorageCapacity.
        :param pulumi.Input[str] storage_class_name: The name of the StorageClass that the reported capacity applies to. It must meet the same requirements as the name of a StorageClass object (non-empty, DNS subdomain). If that object no longer exists, the CSIStorageCapacity object is obsolete and should be removed by its creator. This field is immutable.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] capacity: Capacity is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.
               
               The semantic is currently (CSI spec 1.2) defined as: The available capacity, in bytes, of the storage that can be used to provision volumes. If not set, that information is currently unavailable and treated like zero capacity.
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input[str] maximum_volume_size: MaximumVolumeSize is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.
               
               This is defined since CSI spec 1.4.0 as the largest size that may be used in a CreateVolumeRequest.capacity_range.required_bytes field to create a volume with the same parameters as those in GetCapacityRequest. The corresponding value in the Kubernetes API is ResourceRequirements.Requests in a volume claim.
        :param pulumi.Input['_meta.v1.ObjectMetaArgs'] metadata: Standard object's metadata. The name has no particular meaning. It must be be a DNS subdomain (dots allowed, 253 characters). To ensure that there are no conflicts with other CSI drivers on the cluster, the recommendation is to use csisc-<uuid>, a generated name, or a reverse-domain name which ends with the unique CSI driver name.
               
               Objects are namespaced.
               
               More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param pulumi.Input['_meta.v1.LabelSelectorArgs'] node_topology: NodeTopology defines which nodes have access to the storage for which capacity was reported. If not set, the storage is not accessible from any node in the cluster. If empty, the storage is accessible from all nodes. This field is immutable.
        """
        pulumi.set(__self__, "storage_class_name", storage_class_name)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'storage.k8s.io/v1alpha1')
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if kind is not None:
            pulumi.set(__self__, "kind", 'CSIStorageCapacity')
        if maximum_volume_size is not None:
            pulumi.set(__self__, "maximum_volume_size", maximum_volume_size)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if node_topology is not None:
            pulumi.set(__self__, "node_topology", node_topology)

    @property
    @pulumi.getter(name="storageClassName")
    def storage_class_name(self) -> pulumi.Input[str]:
        """
        The name of the StorageClass that the reported capacity applies to. It must meet the same requirements as the name of a StorageClass object (non-empty, DNS subdomain). If that object no longer exists, the CSIStorageCapacity object is obsolete and should be removed by its creator. This field is immutable.
        """
        return pulumi.get(self, "storage_class_name")

    @storage_class_name.setter
    def storage_class_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_class_name", value)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[str]]:
        """
        Capacity is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.

        The semantic is currently (CSI spec 1.2) defined as: The available capacity, in bytes, of the storage that can be used to provision volumes. If not set, that information is currently unavailable and treated like zero capacity.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "capacity", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="maximumVolumeSize")
    def maximum_volume_size(self) -> Optional[pulumi.Input[str]]:
        """
        MaximumVolumeSize is the value reported by the CSI driver in its GetCapacityResponse for a GetCapacityRequest with topology and parameters that match the previous fields.

        This is defined since CSI spec 1.4.0 as the largest size that may be used in a CreateVolumeRequest.capacity_range.required_bytes field to create a volume with the same parameters as those in GetCapacityRequest. The corresponding value in the Kubernetes API is ResourceRequirements.Requests in a volume claim.
        """
        return pulumi.get(self, "maximum_volume_size")

    @maximum_volume_size.setter
    def maximum_volume_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "maximum_volume_size", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]:
        """
        Standard object's metadata. The name has no particular meaning. It must be be a DNS subdomain (dots allowed, 253 characters). To ensure that there are no conflicts with other CSI drivers on the cluster, the recommendation is to use csisc-<uuid>, a generated name, or a reverse-domain name which ends with the unique CSI driver name.

        Objects are namespaced.

        More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="nodeTopology")
    def node_topology(self) -> Optional[pulumi.Input['_meta.v1.LabelSelectorArgs']]:
        """
        NodeTopology defines which nodes have access to the storage for which capacity was reported. If not set, the storage is not accessible from any node in the cluster. If empty, the storage is accessible from all nodes. This field is immutable.
        """
        return pulumi.get(self, "node_topology")

    @node_topology.setter
    def node_topology(self, value: Optional[pulumi.Input['_meta.v1.LabelSelectorArgs']]):
        pulumi.set(self, "node_topology", value)


@pulumi.input_type
class VolumeAttachmentArgs:
    def __init__(__self__, *,
                 spec: pulumi.Input['VolumeAttachmentSpecArgs'],
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']] = None,
                 status: Optional[pulumi.Input['VolumeAttachmentStatusArgs']] = None):
        """
        VolumeAttachment captures the intent to attach or detach the specified volume to/from the specified node.

        VolumeAttachment objects are non-namespaced.
        :param pulumi.Input['VolumeAttachmentSpecArgs'] spec: Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input['_meta.v1.ObjectMetaArgs'] metadata: Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param pulumi.Input['VolumeAttachmentStatusArgs'] status: Status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher.
        """
        pulumi.set(__self__, "spec", spec)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'storage.k8s.io/v1alpha1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'VolumeAttachment')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Input['VolumeAttachmentSpecArgs']:
        """
        Specification of the desired attach/detach volume behavior. Populated by the Kubernetes system.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: pulumi.Input['VolumeAttachmentSpecArgs']):
        pulumi.set(self, "spec", value)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]:
        """
        Standard object metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['VolumeAttachmentStatusArgs']]:
        """
        Status of the VolumeAttachment request. Populated by the entity completing the attach or detach operation, i.e. the external-attacher.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['VolumeAttachmentStatusArgs']]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class VolumeAttachmentSourceArgs:
    def __init__(__self__, *,
                 inline_volume_spec: Optional[pulumi.Input['_core.v1.PersistentVolumeSpecArgs']] = None,
                 persistent_volume_name: Optional[pulumi.Input[str]] = None):
        """
        VolumeAttachmentSource represents a volume that should be attached. Right now only PersistenVolumes can be attached via external attacher, in future we may allow also inline volumes in pods. Exactly one member can be set.
        :param pulumi.Input['_core.v1.PersistentVolumeSpecArgs'] inline_volume_spec: inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.
        :param pulumi.Input[str] persistent_volume_name: Name of the persistent volume to attach.
        """
        if inline_volume_spec is not None:
            pulumi.set(__self__, "inline_volume_spec", inline_volume_spec)
        if persistent_volume_name is not None:
            pulumi.set(__self__, "persistent_volume_name", persistent_volume_name)

    @property
    @pulumi.getter(name="inlineVolumeSpec")
    def inline_volume_spec(self) -> Optional[pulumi.Input['_core.v1.PersistentVolumeSpecArgs']]:
        """
        inlineVolumeSpec contains all the information necessary to attach a persistent volume defined by a pod's inline VolumeSource. This field is populated only for the CSIMigration feature. It contains translated fields from a pod's inline VolumeSource to a PersistentVolumeSpec. This field is alpha-level and is only honored by servers that enabled the CSIMigration feature.
        """
        return pulumi.get(self, "inline_volume_spec")

    @inline_volume_spec.setter
    def inline_volume_spec(self, value: Optional[pulumi.Input['_core.v1.PersistentVolumeSpecArgs']]):
        pulumi.set(self, "inline_volume_spec", value)

    @property
    @pulumi.getter(name="persistentVolumeName")
    def persistent_volume_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the persistent volume to attach.
        """
        return pulumi.get(self, "persistent_volume_name")

    @persistent_volume_name.setter
    def persistent_volume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "persistent_volume_name", value)


@pulumi.input_type
class VolumeAttachmentSpecArgs:
    def __init__(__self__, *,
                 attacher: pulumi.Input[str],
                 node_name: pulumi.Input[str],
                 source: pulumi.Input['VolumeAttachmentSourceArgs']):
        """
        VolumeAttachmentSpec is the specification of a VolumeAttachment request.
        :param pulumi.Input[str] attacher: Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().
        :param pulumi.Input[str] node_name: The node that the volume should be attached to.
        :param pulumi.Input['VolumeAttachmentSourceArgs'] source: Source represents the volume that should be attached.
        """
        pulumi.set(__self__, "attacher", attacher)
        pulumi.set(__self__, "node_name", node_name)
        pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter
    def attacher(self) -> pulumi.Input[str]:
        """
        Attacher indicates the name of the volume driver that MUST handle this request. This is the name returned by GetPluginName().
        """
        return pulumi.get(self, "attacher")

    @attacher.setter
    def attacher(self, value: pulumi.Input[str]):
        pulumi.set(self, "attacher", value)

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> pulumi.Input[str]:
        """
        The node that the volume should be attached to.
        """
        return pulumi.get(self, "node_name")

    @node_name.setter
    def node_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "node_name", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input['VolumeAttachmentSourceArgs']:
        """
        Source represents the volume that should be attached.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input['VolumeAttachmentSourceArgs']):
        pulumi.set(self, "source", value)


@pulumi.input_type
class VolumeAttachmentStatusArgs:
    def __init__(__self__, *,
                 attached: pulumi.Input[bool],
                 attach_error: Optional[pulumi.Input['VolumeErrorArgs']] = None,
                 attachment_metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 detach_error: Optional[pulumi.Input['VolumeErrorArgs']] = None):
        """
        VolumeAttachmentStatus is the status of a VolumeAttachment request.
        :param pulumi.Input[bool] attached: Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        :param pulumi.Input['VolumeErrorArgs'] attach_error: The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] attachment_metadata: Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        :param pulumi.Input['VolumeErrorArgs'] detach_error: The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.
        """
        pulumi.set(__self__, "attached", attached)
        if attach_error is not None:
            pulumi.set(__self__, "attach_error", attach_error)
        if attachment_metadata is not None:
            pulumi.set(__self__, "attachment_metadata", attachment_metadata)
        if detach_error is not None:
            pulumi.set(__self__, "detach_error", detach_error)

    @property
    @pulumi.getter
    def attached(self) -> pulumi.Input[bool]:
        """
        Indicates the volume is successfully attached. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        """
        return pulumi.get(self, "attached")

    @attached.setter
    def attached(self, value: pulumi.Input[bool]):
        pulumi.set(self, "attached", value)

    @property
    @pulumi.getter(name="attachError")
    def attach_error(self) -> Optional[pulumi.Input['VolumeErrorArgs']]:
        """
        The last error encountered during attach operation, if any. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        """
        return pulumi.get(self, "attach_error")

    @attach_error.setter
    def attach_error(self, value: Optional[pulumi.Input['VolumeErrorArgs']]):
        pulumi.set(self, "attach_error", value)

    @property
    @pulumi.getter(name="attachmentMetadata")
    def attachment_metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Upon successful attach, this field is populated with any information returned by the attach operation that must be passed into subsequent WaitForAttach or Mount calls. This field must only be set by the entity completing the attach operation, i.e. the external-attacher.
        """
        return pulumi.get(self, "attachment_metadata")

    @attachment_metadata.setter
    def attachment_metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "attachment_metadata", value)

    @property
    @pulumi.getter(name="detachError")
    def detach_error(self) -> Optional[pulumi.Input['VolumeErrorArgs']]:
        """
        The last error encountered during detach operation, if any. This field must only be set by the entity completing the detach operation, i.e. the external-attacher.
        """
        return pulumi.get(self, "detach_error")

    @detach_error.setter
    def detach_error(self, value: Optional[pulumi.Input['VolumeErrorArgs']]):
        pulumi.set(self, "detach_error", value)


@pulumi.input_type
class VolumeErrorArgs:
    def __init__(__self__, *,
                 message: Optional[pulumi.Input[str]] = None,
                 time: Optional[pulumi.Input[str]] = None):
        """
        VolumeError captures an error encountered during a volume operation.
        :param pulumi.Input[str] message: String detailing the error encountered during Attach or Detach operation. This string maybe logged, so it should not contain sensitive information.
        :param pulumi.Input[str] time: Time the error was encountered.
        """
        if message is not None:
            pulumi.set(__self__, "message", message)
        if time is not None:
            pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        String detailing the error encountered during Attach or Detach operation. This string maybe logged, so it should not contain sensitive information.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter
    def time(self) -> Optional[pulumi.Input[str]]:
        """
        Time the error was encountered.
        """
        return pulumi.get(self, "time")

    @time.setter
    def time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time", value)


