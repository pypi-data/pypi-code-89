from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EnableWhenBehaviorCode(FhirValueSetBase):
    """
    EnableWhenBehavior
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/questionnaire-enable-behavior
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/questionnaire-enable-behavior"


class EnableWhenBehaviorCodeValues:
    """
    Enable the question when all the enableWhen criteria are satisfied.
    """

    All = EnableWhenBehaviorCode("all")
    """
    Enable the question when any of the enableWhen criteria are satisfied.
    """
    Any = EnableWhenBehaviorCode("any")
