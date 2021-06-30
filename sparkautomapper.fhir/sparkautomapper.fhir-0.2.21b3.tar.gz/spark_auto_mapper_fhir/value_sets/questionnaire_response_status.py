from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class QuestionnaireResponseStatusCode(FhirValueSetBase):
    """
    QuestionnaireResponseStatus
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/questionnaire-answers-status
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/questionnaire-answers-status"


class QuestionnaireResponseStatusCodeValues:
    """
    This QuestionnaireResponse has been partially filled out with answers but changes or additions are still expected to be made to it.
    """

    InProgress = QuestionnaireResponseStatusCode("in-progress")
    """
    This QuestionnaireResponse has been filled out with answers and the current content is regarded as definitive.
    """
    Completed = QuestionnaireResponseStatusCode("completed")
    """
    This QuestionnaireResponse has been filled out with answers, then marked as complete, yet changes or additions have been made to it afterwards.
    """
    Amended = QuestionnaireResponseStatusCode("amended")
    """
    This QuestionnaireResponse was entered in error and voided.
    """
    EnteredInError = QuestionnaireResponseStatusCode("entered-in-error")
    """
    This QuestionnaireResponse has been partially filled out with answers but has been abandoned. It is unknown whether changes or additions are expected to be made to it.
    """
    Stopped = QuestionnaireResponseStatusCode("stopped")
