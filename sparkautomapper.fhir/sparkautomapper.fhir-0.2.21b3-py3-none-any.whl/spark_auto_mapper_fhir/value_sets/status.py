from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class StatusCode(FhirValueSetBase):
    """
    status
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/verificationresult-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/verificationresult-status"


class StatusCodeValues:
    """
    ***TODO***
    """

    Attested = StatusCode("attested")
    """
    ***TODO***
    """
    Validated = StatusCode("validated")
    """
    ***TODO***
    """
    InProcess = StatusCode("in-process")
    """
    ***TODO***
    """
    RequiresRevalidation = StatusCode("req-revalid")
    """
    ***TODO***
    """
    ValidationFailed = StatusCode("val-fail")
    """
    ***TODO***
    """
    Re_ValidationFailed = StatusCode("reval-fail")
