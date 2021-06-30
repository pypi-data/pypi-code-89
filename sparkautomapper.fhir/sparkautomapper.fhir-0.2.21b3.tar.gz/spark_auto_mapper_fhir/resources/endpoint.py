from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.endpoint import EndpointSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # status (EndpointStatus)
    from spark_auto_mapper_fhir.value_sets.endpoint_status import EndpointStatusCode

    # connectionType (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for connectionType
    from spark_auto_mapper_fhir.value_sets.endpoint_connection_type import (
        EndpointConnectionTypeCode,
    )

    # End Import for CodeableConcept for connectionType
    # name (string)
    # managingOrganization (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for managingOrganization
    from spark_auto_mapper_fhir.resources.organization import Organization

    # contact (ContactPoint)
    from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # payloadType (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for payloadType
    from spark_auto_mapper_fhir.value_sets.endpoint_payload_type import (
        EndpointPayloadTypeCode,
    )

    # End Import for CodeableConcept for payloadType
    # payloadMimeType (Mime Types)
    from spark_auto_mapper_fhir.value_sets.mime_types import MimeTypesCode

    # address (url)
    from spark_auto_mapper_fhir.complex_types.url import url

    # header (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Endpoint(FhirResourceBase):
    """
    Endpoint
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: EndpointStatusCode,
        connectionType: Coding[EndpointConnectionTypeCode],
        name: Optional[FhirString] = None,
        managingOrganization: Optional[Reference[Union[Organization]]] = None,
        contact: Optional[FhirList[ContactPoint]] = None,
        period: Optional[Period] = None,
        payloadType: FhirList[CodeableConcept[EndpointPayloadTypeCode]],
        payloadMimeType: Optional[FhirList[MimeTypesCode]] = None,
        address: url,
        header: Optional[FhirList[FhirString]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Identifier for the organization that is used to identify the endpoint across
        multiple disparate systems.
            :param status: active | suspended | error | off | test.
            :param connectionType: A coded value that represents the technical details of the usage of this
        endpoint, such as what WSDLs should be used in what way. (e.g.
        XDS.b/DICOM/cds-hook).
            :param name: A friendly name that this endpoint can be referred to with.
            :param managingOrganization: The organization that manages this endpoint (even if technically another
        organization is hosting this in the cloud, it is the organization associated
        with the data).
            :param contact: Contact details for a human to contact about the subscription. The primary use
        of this for system administrator troubleshooting.
            :param period: The interval during which the endpoint is expected to be operational.
            :param payloadType: The payload type describes the acceptable content that can be communicated on
        the endpoint.
            :param payloadMimeType: The mime type to send the payload in - e.g. application/fhir+xml,
        application/fhir+json. If the mime type is not specified, then the sender
        could send any content (including no content depending on the connectionType).
            :param address: The uri that describes the actual end-point to connect to.
            :param header: Additional headers / information to send as part of the notification.
        """
        super().__init__(
            resourceType="Endpoint",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            connectionType=connectionType,
            name=name,
            managingOrganization=managingOrganization,
            contact=contact,
            period=period,
            payloadType=payloadType,
            payloadMimeType=payloadMimeType,
            address=address,
            header=header,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return EndpointSchema.get_schema(include_extension=include_extension)
