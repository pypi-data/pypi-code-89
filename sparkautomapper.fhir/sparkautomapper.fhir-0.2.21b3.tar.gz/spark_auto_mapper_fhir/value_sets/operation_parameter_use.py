from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class OperationParameterUseCode(FhirValueSetBase):
    """
    OperationParameterUse
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/operation-parameter-use
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/operation-parameter-use"


class OperationParameterUseCodeValues:
    """
    This is an input parameter.
    """

    In = OperationParameterUseCode("in")
    """
    This is an output parameter.
    """
    Out = OperationParameterUseCode("out")
