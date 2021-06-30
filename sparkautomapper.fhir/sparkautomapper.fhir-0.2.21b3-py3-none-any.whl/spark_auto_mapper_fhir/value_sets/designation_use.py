from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DesignationUseCode(FhirValueSetBase):
    """
    DesignationUse
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/designation-use
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/designation-use"


class DesignationUseCodeValues:
    """
    None
    """

    _900000000000003001 = DesignationUseCode("900000000000003001")
    """
    None
    """
    _900000000000013009 = DesignationUseCode("900000000000013009")
