from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ConditionalReadStatusCode(FhirValueSetBase):
    """
    ConditionalReadStatus
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/conditional-read-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/conditional-read-status"


class ConditionalReadStatusCodeValues:
    """
    No support for conditional reads.
    """

    NotSupported = ConditionalReadStatusCode("not-supported")
    """
    Conditional reads are supported, but only with the If-Modified-Since HTTP Header.
    """
    If_Modified_Since = ConditionalReadStatusCode("modified-since")
    """
    Conditional reads are supported, but only with the If-None-Match HTTP Header.
    """
    If_None_Match = ConditionalReadStatusCode("not-match")
    """
    Conditional reads are supported, with both If-Modified-Since and If-None-Match HTTP Headers.
    """
    FullSupport = ConditionalReadStatusCode("full-support")
