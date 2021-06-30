from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class GeneralPurposeOfUse(FhirValueSetBase):
    """
    GeneralPurposeOfUse
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/ValueSet/v3-GeneralPurposeOfUse
    """
    codeset: FhirUri = "http://terminology.hl7.org/ValueSet/v3-GeneralPurposeOfUse"
