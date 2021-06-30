from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class IssueTypeCode(FhirValueSetBase):
    """
    IssueType
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/issue-type
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/issue-type"


class IssueTypeCodeValues:
    """
    Content invalid against the specification or a profile.
    """

    InvalidContent = IssueTypeCode("invalid")
    """
    An authentication/authorization/permissions issue of some kind.
    """
    SecurityProblem = IssueTypeCode("security")
    """
    Processing issues. These are expected to be final e.g. there is no point resubmitting the same content unchanged.
    """
    ProcessingFailure = IssueTypeCode("processing")
    """
    Transient processing issues. The system receiving the message may be able to resubmit the same content once an underlying issue is resolved.
    """
    TransientIssue = IssueTypeCode("transient")
    """
    A message unrelated to the processing success of the completed operation (examples of the latter include things like reminders of password expiry, system maintenance times, etc.).
    """
    InformationalNote = IssueTypeCode("informational")
