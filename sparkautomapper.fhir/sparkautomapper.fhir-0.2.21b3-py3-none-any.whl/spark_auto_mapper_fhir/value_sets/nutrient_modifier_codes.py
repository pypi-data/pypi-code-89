from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class NutrientModifierCodesCode(FhirValueSetBase):
    """
    NutrientModifierCodes
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/nutrient-code
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/nutrient-code"


class NutrientModifierCodesCodeValues:
    """
    None
    """

    Fluid = NutrientModifierCodesCode("33463005")
    """
    None
    """
    Sodium = NutrientModifierCodesCode("39972003")
    """
    None
    """
    Potassium = NutrientModifierCodesCode("88480006")
