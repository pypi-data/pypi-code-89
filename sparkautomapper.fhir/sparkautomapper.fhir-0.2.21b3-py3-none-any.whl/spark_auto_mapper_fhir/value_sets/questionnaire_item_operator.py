from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class QuestionnaireItemOperatorCode(FhirValueSetBase):
    """
    QuestionnaireItemOperator
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/questionnaire-enable-operator
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/questionnaire-enable-operator"


class QuestionnaireItemOperatorCodeValues:
    """
    True if whether an answer exists is equal to the enableWhen answer (which must be a boolean).
    """

    Exists = QuestionnaireItemOperatorCode("exists")
    """
    True if whether at least one answer has a value that is equal to the enableWhen answer.
    """
    Equals = QuestionnaireItemOperatorCode("=")
    """
    True if whether at least no answer has a value that is equal to the enableWhen answer.
    """
    NotEquals = QuestionnaireItemOperatorCode("!=")
    """
    True if whether at least no answer has a value that is greater than the enableWhen answer.
    """
    GreaterThan = QuestionnaireItemOperatorCode(">")
    """
    True if whether at least no answer has a value that is less than the enableWhen answer.
    """
    LessThan = QuestionnaireItemOperatorCode("<")
    """
    True if whether at least no answer has a value that is greater or equal to the enableWhen answer.
    """
    GreaterOrEquals = QuestionnaireItemOperatorCode(">=")
    """
    True if whether at least no answer has a value that is less or equal to the enableWhen answer.
    """
    LessOrEquals = QuestionnaireItemOperatorCode("<=")
