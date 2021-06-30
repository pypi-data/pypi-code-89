from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class GoalLifecycleStatusCode(FhirValueSetBase):
    """
    GoalLifecycleStatus
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/goal-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/goal-status"


class GoalLifecycleStatusCodeValues:
    """
    A goal is proposed for this patient.
    """

    Proposed = GoalLifecycleStatusCode("proposed")
    """
    A goal is planned for this patient.
    """
    Planned = GoalLifecycleStatusCode("planned")
    """
    A proposed goal was accepted or acknowledged.
    """
    Accepted = GoalLifecycleStatusCode("accepted")
    """
    The goal has been abandoned.
    """
    Cancelled = GoalLifecycleStatusCode("cancelled")
    """
    The goal was entered in error and voided.
    """
    EnteredInError = GoalLifecycleStatusCode("entered-in-error")
    """
    A proposed goal was rejected.
    """
    Rejected = GoalLifecycleStatusCode("rejected")
