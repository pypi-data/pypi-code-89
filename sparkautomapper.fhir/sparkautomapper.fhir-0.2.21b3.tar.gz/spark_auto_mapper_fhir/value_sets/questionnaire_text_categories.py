from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class QuestionnaireTextCategoriesCode(FhirValueSetBase):
    """
    QuestionnaireTextCategories
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/questionnaire-display-category
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/questionnaire-display-category"


class QuestionnaireTextCategoriesCodeValues:
    """
    The text provides guidance on how to populate or use a portion of the questionnaire (or the questionnaire as a whole).
    """

    Instructions = QuestionnaireTextCategoriesCode("instructions")
    """
    The text provides guidance on how the information should be or will be handled from a security/confidentiality/access control perspective when completed
    """
    Security = QuestionnaireTextCategoriesCode("security")
    """
    The text provides additional guidance on populating the containing item.  Help text isn't necessarily expected to be rendered as part of the form, but may instead be made available through fly-over, pop-up button, link to a "help" page, etc.
    """
    Help = QuestionnaireTextCategoriesCode("help")
