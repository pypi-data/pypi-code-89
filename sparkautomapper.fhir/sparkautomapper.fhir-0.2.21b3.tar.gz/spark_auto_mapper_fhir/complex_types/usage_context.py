from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase

if TYPE_CHECKING:
    pass
    # code (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.usage_context_type import (
        UsageContextTypeCode,
    )

    # End Import for CodeableConcept for code
    # valueCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for valueCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for valueCodeableConcept
    # valueQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # valueRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # valueReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for valueReference
    from spark_auto_mapper_fhir.resources.plan_definition import PlanDefinition
    from spark_auto_mapper_fhir.resources.research_study import ResearchStudy
    from spark_auto_mapper_fhir.resources.insurance_plan import InsurancePlan
    from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.location import Location
    from spark_auto_mapper_fhir.resources.organization import Organization


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class UsageContext(FhirComplexTypeBase):
    """
    UsageContext
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        code: Coding[UsageContextTypeCode],
        valueCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        valueQuantity: Optional[Quantity] = None,
        valueRange: Optional[Range] = None,
        valueReference: Optional[
            Reference[
                Union[
                    PlanDefinition,
                    ResearchStudy,
                    InsurancePlan,
                    HealthcareService,
                    Group,
                    Location,
                    Organization,
                ]
            ]
        ] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param code: A code that identifies the type of context being specified by this usage
        context.
            :param valueCodeableConcept: None
            :param valueQuantity: None
            :param valueRange: None
            :param valueReference: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            valueCodeableConcept=valueCodeableConcept,
            valueQuantity=valueQuantity,
            valueRange=valueRange,
            valueReference=valueReference,
        )
