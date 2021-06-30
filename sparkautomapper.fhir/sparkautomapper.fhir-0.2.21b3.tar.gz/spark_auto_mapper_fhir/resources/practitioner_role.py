from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.practitionerrole import PractitionerRoleSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # active (boolean)
    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # practitioner (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for practitioner
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner

    # organization (Reference)
    # Imports for References for organization
    from spark_auto_mapper_fhir.resources.organization import Organization

    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.practitioner_role import PractitionerRoleCode

    # End Import for CodeableConcept for code
    # specialty (CodeableConcept)
    # Import for CodeableConcept for specialty
    from spark_auto_mapper_fhir.value_sets.practice_setting_code_value_set import (
        PracticeSettingCodeValueSetCode,
    )

    # End Import for CodeableConcept for specialty
    # location (Reference)
    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location

    # healthcareService (Reference)
    # Imports for References for healthcareService
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService

    # telecom (ContactPoint)
    from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

    # availableTime (PractitionerRole.AvailableTime)
    from spark_auto_mapper_fhir.backbone_elements.practitioner_role_available_time import (
        PractitionerRoleAvailableTime,
    )

    # notAvailable (PractitionerRole.NotAvailable)
    from spark_auto_mapper_fhir.backbone_elements.practitioner_role_not_available import (
        PractitionerRoleNotAvailable,
    )

    # availabilityExceptions (string)
    # endpoint (Reference)
    # Imports for References for endpoint
    from spark_auto_mapper_fhir.resources.endpoint import Endpoint


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PractitionerRole(FhirResourceBase):
    """
    PractitionerRole
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        active: Optional[FhirBoolean] = None,
        period: Optional[Period] = None,
        practitioner: Optional[Reference[Union[Practitioner]]] = None,
        organization: Optional[Reference[Union[Organization]]] = None,
        code: Optional[FhirList[CodeableConcept[PractitionerRoleCode]]] = None,
        specialty: Optional[
            FhirList[CodeableConcept[PracticeSettingCodeValueSetCode]]
        ] = None,
        location: Optional[FhirList[Reference[Union[Location]]]] = None,
        healthcareService: Optional[
            FhirList[Reference[Union[HealthcareService]]]
        ] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        availableTime: Optional[FhirList[PractitionerRoleAvailableTime]] = None,
        notAvailable: Optional[FhirList[PractitionerRoleNotAvailable]] = None,
        availabilityExceptions: Optional[FhirString] = None,
        endpoint: Optional[FhirList[Reference[Union[Endpoint]]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Business Identifiers that are specific to a role/location.
            :param active: Whether this practitioner role record is in active use.
            :param period: The period during which the person is authorized to act as a practitioner in
        these role(s) for the organization.
            :param practitioner: Practitioner that is able to provide the defined services for the
        organization.
            :param organization: The organization where the Practitioner performs the roles associated.
            :param code: Roles which this practitioner is authorized to perform for the organization.
            :param specialty: Specific specialty of the practitioner.
            :param location: The location(s) at which this practitioner provides care.
            :param healthcareService: The list of healthcare services that this worker provides for this role's
        Organization/Location(s).
            :param telecom: Contact details that are specific to the role/location/service.
            :param availableTime: A collection of times the practitioner is available or performing this role at
        the location and/or healthcareservice.
            :param notAvailable: The practitioner is not available or performing this role during this period
        of time due to the provided reason.
            :param availabilityExceptions: A description of site availability exceptions, e.g. public holiday
        availability. Succinctly describing all possible exceptions to normal site
        availability as details in the available Times and not available Times.
            :param endpoint: Technical endpoints providing access to services operated for the practitioner
        with this role.
        """
        super().__init__(
            resourceType="PractitionerRole",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            active=active,
            period=period,
            practitioner=practitioner,
            organization=organization,
            code=code,
            specialty=specialty,
            location=location,
            healthcareService=healthcareService,
            telecom=telecom,
            availableTime=availableTime,
            notAvailable=notAvailable,
            availabilityExceptions=availabilityExceptions,
            endpoint=endpoint,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return PractitionerRoleSchema.get_schema(include_extension=include_extension)
