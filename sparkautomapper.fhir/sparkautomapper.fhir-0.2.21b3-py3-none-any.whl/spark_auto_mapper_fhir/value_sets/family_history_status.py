from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class FamilyHistoryStatusCode(FhirValueSetBase):
    """
    FamilyHistoryStatus
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/history-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/history-status"


class FamilyHistoryStatusCodeValues:
    """
    Some health information is known and captured, but not complete - see notes for details.
    """

    Partial = FamilyHistoryStatusCode("partial")
    """
    All available related health information is captured as of the date (and possibly time) when the family member history was taken.
    """
    Completed = FamilyHistoryStatusCode("completed")
    """
    This instance should not have been part of this patient's medical record.
    """
    EnteredInError = FamilyHistoryStatusCode("entered-in-error")
    """
    Health information for this family member is unavailable/unknown.
    """
    HealthUnknown = FamilyHistoryStatusCode("health-unknown")
