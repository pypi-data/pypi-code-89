from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SupplyRequestStatusCode(FhirValueSetBase):
    """
    SupplyRequestStatus
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/supplyrequest-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/supplyrequest-status"


class SupplyRequestStatusCodeValues:
    """
    The request has been created but is not yet complete or ready for action.
    """

    Draft = SupplyRequestStatusCode("draft")
    """
    The request is ready to be acted upon.
    """
    Active = SupplyRequestStatusCode("active")
    """
    The authorization/request to act has been temporarily withdrawn but is expected to resume in the future.
    """
    Suspended = SupplyRequestStatusCode("suspended")
    """
    The authorization/request to act has been terminated prior to the full completion of the intended actions.  No further activity should occur.
    """
    Cancelled = SupplyRequestStatusCode("cancelled")
    """
    Activity against the request has been sufficiently completed to the satisfaction of the requester.
    """
    Completed = SupplyRequestStatusCode("completed")
    """
    This electronic record should never have existed, though it is possible that real-world decisions were based on it.  (If real-world activity has occurred, the status should be "cancelled" rather than "entered-in-error".).
    """
    EnteredInError = SupplyRequestStatusCode("entered-in-error")
    """
    The authoring/source system does not know which of the status values currently applies for this observation. Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but the authoring/source system does not know which.
    """
    Unknown = SupplyRequestStatusCode("unknown")
