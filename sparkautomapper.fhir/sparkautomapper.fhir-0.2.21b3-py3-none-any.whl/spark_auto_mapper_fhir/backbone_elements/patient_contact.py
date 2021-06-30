from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # relationship (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for relationship
    # Import for CodeableConcept for relationship
    from spark_auto_mapper_fhir.value_sets.patient_contact_relationship import (
        PatientContactRelationshipCode,
    )

    # End Import for CodeableConcept for relationship
    # name (HumanName)
    from spark_auto_mapper_fhir.complex_types.human_name import HumanName

    # telecom (ContactPoint)
    from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

    # address (Address)
    from spark_auto_mapper_fhir.complex_types.address import Address

    # gender (AdministrativeGender)
    from spark_auto_mapper_fhir.value_sets.administrative_gender import (
        AdministrativeGenderCode,
    )

    # organization (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for organization
    from spark_auto_mapper_fhir.resources.organization import Organization

    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PatientContact(FhirBackboneElementBase):
    """
    Patient.Contact
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        relationship: Optional[
            FhirList[CodeableConcept[PatientContactRelationshipCode]]
        ] = None,
        name: Optional[HumanName] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        address: Optional[Address] = None,
        gender: Optional[AdministrativeGenderCode] = None,
        organization: Optional[Reference[Union[Organization]]] = None,
        period: Optional[Period] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param relationship: The nature of the relationship between the patient and the contact person.
            :param name: A name associated with the contact person.
            :param telecom: A contact detail for the person, e.g. a telephone number or an email address.
            :param address: Address for the contact person.
            :param gender: Administrative Gender - the gender that the contact person is considered to
        have for administration and record keeping purposes.
            :param organization: Organization on behalf of which the contact is acting or for which the contact
        is working.
            :param period: The period during which this contact person or organization is valid to be
        contacted relating to this patient.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            relationship=relationship,
            name=name,
            telecom=telecom,
            address=address,
            gender=gender,
            organization=organization,
            period=period,
        )
