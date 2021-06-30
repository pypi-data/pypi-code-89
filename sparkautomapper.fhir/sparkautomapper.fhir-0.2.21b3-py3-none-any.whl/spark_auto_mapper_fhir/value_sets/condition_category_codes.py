from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ConditionCategoryCodesCode(FhirValueSetBase):
    """
    ConditionCategoryCodes
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/condition-category
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/condition-category"


class ConditionCategoryCodesCodeValues:
    """
    An item on a problem list that can be managed over time and can be expressed by a practitioner (e.g. physician, nurse), patient, or related person.
    """

    ProblemListItem = ConditionCategoryCodesCode("problem-list-item")
    """
    A point in time diagnosis (e.g. from a physician or nurse) in context of an encounter.
    """
    EncounterDiagnosis = ConditionCategoryCodesCode("encounter-diagnosis")
