from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExampleMessageReasonCodesCode(FhirValueSetBase):
    """
    ExampleMessageReasonCodes
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/message-reason-encounter
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/message-reason-encounter"


class ExampleMessageReasonCodesCodeValues:
    """
    The patient has been admitted.
    """

    Admit = ExampleMessageReasonCodesCode("admit")
    """
    The patient has been discharged.
    """
    Discharge = ExampleMessageReasonCodesCode("discharge")
    """
    The patient has temporarily left the institution.
    """
    Absent = ExampleMessageReasonCodesCode("absent")
    """
    The patient has returned from a temporary absence.
    """
    Returned = ExampleMessageReasonCodesCode("return")
    """
    The patient has been moved to a new location.
    """
    Moved = ExampleMessageReasonCodesCode("moved")
    """
    Encounter details have been updated (e.g. to correct a coding error).
    """
    Edit = ExampleMessageReasonCodesCode("edit")
