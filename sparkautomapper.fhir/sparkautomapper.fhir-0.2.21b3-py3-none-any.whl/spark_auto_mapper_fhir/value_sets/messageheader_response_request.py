from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Messageheader_response_requestCode(FhirValueSetBase):
    """
    messageheader-response-request
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/messageheader-response-request
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/messageheader-response-request"


class Messageheader_response_requestCodeValues:
    """
    initiator expects a response for this message.
    """

    Always = Messageheader_response_requestCode("always")
    """
    initiator expects a response only if in error.
    """
    Error_rejectConditionsOnly = Messageheader_response_requestCode("on-error")
    """
    initiator does not expect a response.
    """
    Never = Messageheader_response_requestCode("never")
    """
    initiator expects a response only if successful.
    """
    SuccessfulCompletionOnly = Messageheader_response_requestCode("on-success")
