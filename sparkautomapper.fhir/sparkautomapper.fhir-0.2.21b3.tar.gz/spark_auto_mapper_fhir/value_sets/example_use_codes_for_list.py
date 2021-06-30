from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExampleUseCodesForListCode(FhirValueSetBase):
    """
    ExampleUseCodesForList
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/list-example-codes
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/list-example-codes"


class ExampleUseCodesForListCodeValues:
    """
    A list of alerts for the patient.
    """

    Alerts = ExampleUseCodesForListCode("alerts")
    """
    A list of part adverse reactions.
    """
    AdverseReactions = ExampleUseCodesForListCode("adverserxns")
    """
    A list of Allergies for the patient.
    """
    Allergies = ExampleUseCodesForListCode("allergies")
    """
    A list of medication statements for the patient.
    """
    MedicationList = ExampleUseCodesForListCode("medications")
    """
    A list of problems that the patient is known of have (or have had in the past).
    """
    ProblemList = ExampleUseCodesForListCode("problems")
    """
    A list of items that constitute a set of work to be performed (typically this code would be specialized for more specific uses, such as a ward round list).
    """
    Worklist = ExampleUseCodesForListCode("worklist")
    """
    A list of items waiting for an event (perhaps a surgical patient waiting list).
    """
    WaitingList = ExampleUseCodesForListCode("waiting")
    """
    A set of protocols to be followed.
    """
    Protocols = ExampleUseCodesForListCode("protocols")
    """
    A set of care plans that apply in a particular context of care.
    """
    CarePlans = ExampleUseCodesForListCode("plans")
