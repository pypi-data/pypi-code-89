from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ListEmptyReasonsCode(FhirValueSetBase):
    """
    ListEmptyReasons
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/list-empty-reason
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/list-empty-reason"


class ListEmptyReasonsCodeValues:
    """
    Clinical judgment that there are no known items for this list after reasonable investigation. Note that this a positive statement by a clinical user, and not a default position asserted by a computer system in the lack of other information. Example uses:  * For allergies: the patient or patient's agent/guardian has asserted that he/she is not aware of any allergies (NKA - nil known allergies)  * For medications: the patient or patient's agent/guardian has asserted that the patient is known to be taking no medications  * For diagnoses, problems and procedures: the patient or patient's agent/guardian has asserted that there is no known event to record.
    """

    NilKnown = ListEmptyReasonsCode("nilknown")
    """
    The investigation to find out whether there are items for this list has not occurred.
    """
    NotAsked = ListEmptyReasonsCode("notasked")
    """
    The content of the list was not provided due to privacy or confidentiality concerns. Note that it should not be assumed that this means that the particular information in question was withheld due to its contents - it can also be a policy decision.
    """
    InformationWithheld = ListEmptyReasonsCode("withheld")
    """
    Information to populate this list cannot be obtained; e.g. unconscious patient.
    """
    Unavailable = ListEmptyReasonsCode("unavailable")
    """
    The work to populate this list has not yet begun.
    """
    NotStarted = ListEmptyReasonsCode("notstarted")
    """
    This list has now closed or has ceased to be relevant or useful.
    """
    Closed = ListEmptyReasonsCode("closed")
