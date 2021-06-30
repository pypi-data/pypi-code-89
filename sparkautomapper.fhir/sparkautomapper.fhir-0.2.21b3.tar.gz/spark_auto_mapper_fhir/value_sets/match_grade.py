from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MatchGradeCode(FhirValueSetBase):
    """
    MatchGrade
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/match-grade
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/match-grade"


class MatchGradeCodeValues:
    """
    This record meets the matching criteria to be automatically considered as a full match.
    """

    CertainMatch = MatchGradeCode("certain")
    """
    This record is a close match, but not a certain match. Additional review (e.g. by a human) may be required before using this as a match.
    """
    ProbableMatch = MatchGradeCode("probable")
    """
    This record may be a matching one. Additional review (e.g. by a human) SHOULD be performed before using this as a match.
    """
    PossibleMatch = MatchGradeCode("possible")
    """
    This record is known not to be a match. Note that usually non-matching records are not returned, but in some cases records previously or likely considered as a match may specifically be negated by the matching engine.
    """
    CertainlyNotAMatch = MatchGradeCode("certainly-not")
