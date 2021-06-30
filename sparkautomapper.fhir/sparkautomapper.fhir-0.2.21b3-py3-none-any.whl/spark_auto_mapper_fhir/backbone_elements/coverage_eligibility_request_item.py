from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.resource import Resource

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # supportingInfoSequence (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # category (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for category
    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.benefit_category_codes import (
        BenefitCategoryCodesCode,
    )

    # End Import for CodeableConcept for category
    # productOrService (CodeableConcept)
    # End Import for References for productOrService
    # Import for CodeableConcept for productOrService
    from spark_auto_mapper_fhir.value_sets.uscls_codes import USCLSCodesCode

    # End Import for CodeableConcept for productOrService
    # modifier (CodeableConcept)
    # End Import for References for modifier
    # Import for CodeableConcept for modifier
    from spark_auto_mapper_fhir.value_sets.modifier_type_codes import (
        ModifierTypeCodesCode,
    )

    # End Import for CodeableConcept for modifier
    # provider (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for provider
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # unitPrice (Money)
    from spark_auto_mapper_fhir.complex_types.money import Money

    # facility (Reference)
    # Imports for References for facility
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.resources.organization import Organization

    # diagnosis (CoverageEligibilityRequest.Diagnosis)
    from spark_auto_mapper_fhir.backbone_elements.coverage_eligibility_request_diagnosis import (
        CoverageEligibilityRequestDiagnosis,
    )

    # detail (Reference)
    # Imports for References for detail


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CoverageEligibilityRequestItem(FhirBackboneElementBase):
    """
    CoverageEligibilityRequest.Item
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        supportingInfoSequence: Optional[FhirList[FhirPositiveInt]] = None,
        category: Optional[CodeableConcept[BenefitCategoryCodesCode]] = None,
        productOrService: Optional[CodeableConcept[USCLSCodesCode]] = None,
        modifier: Optional[FhirList[CodeableConcept[ModifierTypeCodesCode]]] = None,
        provider: Optional[Reference[Union[Practitioner, PractitionerRole]]] = None,
        quantity: Optional[Quantity] = None,
        unitPrice: Optional[Money] = None,
        facility: Optional[Reference[Union[Location, Organization]]] = None,
        diagnosis: Optional[FhirList[CoverageEligibilityRequestDiagnosis]] = None,
        detail: Optional[FhirList[Reference[Union[Resource]]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param supportingInfoSequence: Exceptions, special conditions and supporting information applicable for this
        service or product line.
            :param category: Code to identify the general type of benefits under which products and
        services are provided.
            :param productOrService: This contains the product, service, drug or other billing code for the item.
            :param modifier: Item typification or modifiers codes to convey additional context for the
        product or service.
            :param provider: The practitioner who is responsible for the product or service to be rendered
        to the patient.
            :param quantity: The number of repetitions of a service or product.
            :param unitPrice: The amount charged to the patient by the provider for a single unit.
            :param facility: Facility where the services will be provided.
            :param diagnosis: Patient diagnosis for which care is sought.
            :param detail: The plan/proposal/order describing the proposed service in detail.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            supportingInfoSequence=supportingInfoSequence,
            category=category,
            productOrService=productOrService,
            modifier=modifier,
            provider=provider,
            quantity=quantity,
            unitPrice=unitPrice,
            facility=facility,
            diagnosis=diagnosis,
            detail=detail,
        )
