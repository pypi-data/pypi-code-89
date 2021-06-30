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
from spark_fhir_schemas.r4.resources.location import LocationSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # status (LocationStatus)
    from spark_auto_mapper_fhir.value_sets.location_status import LocationStatusCode

    # operationalStatus (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for operationalStatus
    from spark_auto_mapper_fhir.value_sets.v2_0116 import V2_0116

    # End Import for CodeableConcept for operationalStatus
    # name (string)
    # alias (string)
    # description (string)
    # mode (LocationMode)
    from spark_auto_mapper_fhir.value_sets.location_mode import LocationModeCode

    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.service_delivery_location_role_type import (
        ServiceDeliveryLocationRoleType,
    )

    # End Import for CodeableConcept for type_
    # telecom (ContactPoint)
    from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

    # address (Address)
    from spark_auto_mapper_fhir.complex_types.address import Address

    # physicalType (CodeableConcept)
    # Import for CodeableConcept for physicalType
    from spark_auto_mapper_fhir.value_sets.location_type import LocationTypeCode

    # End Import for CodeableConcept for physicalType
    # position (Location.Position)
    from spark_auto_mapper_fhir.backbone_elements.location_position import (
        LocationPosition,
    )

    # managingOrganization (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for managingOrganization
    from spark_auto_mapper_fhir.resources.organization import Organization

    # partOf (Reference)
    # Imports for References for partOf
    # hoursOfOperation (Location.HoursOfOperation)
    from spark_auto_mapper_fhir.backbone_elements.location_hours_of_operation import (
        LocationHoursOfOperation,
    )

    # availabilityExceptions (string)
    # endpoint (Reference)
    # Imports for References for endpoint
    from spark_auto_mapper_fhir.resources.endpoint import Endpoint


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Location(FhirResourceBase):
    """
    Location
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: Optional[LocationStatusCode] = None,
        operationalStatus: Optional[Coding[V2_0116]] = None,
        name: Optional[FhirString] = None,
        alias: Optional[FhirList[FhirString]] = None,
        description: Optional[FhirString] = None,
        mode: Optional[LocationModeCode] = None,
        type_: Optional[
            FhirList[CodeableConcept[ServiceDeliveryLocationRoleType]]
        ] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        address: Optional[Address] = None,
        physicalType: Optional[CodeableConcept[LocationTypeCode]] = None,
        position: Optional[LocationPosition] = None,
        managingOrganization: Optional[Reference[Union[Organization]]] = None,
        partOf: Optional[Reference[Union[Location]]] = None,
        hoursOfOperation: Optional[FhirList[LocationHoursOfOperation]] = None,
        availabilityExceptions: Optional[FhirString] = None,
        endpoint: Optional[FhirList[Reference[Union[Endpoint]]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Unique code or number identifying the location to its users.
            :param status: The status property covers the general availability of the resource, not the
        current value which may be covered by the operationStatus, or by a
        schedule/slots if they are configured for the location.
            :param operationalStatus: The operational status covers operation values most relevant to beds (but can
        also apply to rooms/units/chairs/etc. such as an isolation unit/dialysis
        chair). This typically covers concepts such as contamination, housekeeping,
        and other activities like maintenance.
            :param name: Name of the location as used by humans. Does not need to be unique.
            :param alias: A list of alternate names that the location is known as, or was known as, in
        the past.
            :param description: Description of the Location, which helps in finding or referencing the place.
            :param mode: Indicates whether a resource instance represents a specific location or a
        class of locations.
            :param type_: Indicates the type of function performed at the location.
            :param telecom: The contact details of communication devices available at the location. This
        can include phone numbers, fax numbers, mobile numbers, email addresses and
        web sites.
            :param address: Physical location.
            :param physicalType: Physical form of the location, e.g. building, room, vehicle, road.
            :param position: The absolute geographic location of the Location, expressed using the WGS84
        datum (This is the same co-ordinate system used in KML).
            :param managingOrganization: The organization responsible for the provisioning and upkeep of the location.
            :param partOf: Another Location of which this Location is physically a part of.
            :param hoursOfOperation: What days/times during a week is this location usually open.
            :param availabilityExceptions: A description of when the locations opening ours are different to normal, e.g.
        public holiday availability. Succinctly describing all possible exceptions to
        normal site availability as detailed in the opening hours Times.
            :param endpoint: Technical endpoints providing access to services operated for the location.
        """
        super().__init__(
            resourceType="Location",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            operationalStatus=operationalStatus,
            name=name,
            alias=alias,
            description=description,
            mode=mode,
            type_=type_,
            telecom=telecom,
            address=address,
            physicalType=physicalType,
            position=position,
            managingOrganization=managingOrganization,
            partOf=partOf,
            hoursOfOperation=hoursOfOperation,
            availabilityExceptions=availabilityExceptions,
            endpoint=endpoint,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return LocationSchema.get_schema(include_extension=include_extension)
