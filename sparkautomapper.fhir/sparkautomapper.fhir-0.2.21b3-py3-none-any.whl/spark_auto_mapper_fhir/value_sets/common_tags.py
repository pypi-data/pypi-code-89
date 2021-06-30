from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CommonTagsCode(FhirValueSetBase):
    """
    CommonTags
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/common-tags
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/common-tags"


class CommonTagsCodeValues:
    """
    This request is intended to be acted upon, not merely stored
    """

    Actionable = CommonTagsCode("actionable")
