from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class GroupMeasureCode(FhirValueSetBase):
    """
    GroupMeasure
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/group-measure
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/group-measure"


class GroupMeasureCodeValues:
    """
    Aggregated using Mean of participant values.
    """

    Mean = GroupMeasureCode("mean")
    """
    Aggregated using Median of participant values.
    """
    Median = GroupMeasureCode("median")
    """
    Aggregated using Mean of study mean values.
    """
    MeanOfStudyMeans = GroupMeasureCode("mean-of-mean")
    """
    Aggregated using Mean of study median values.
    """
    MeanOfStudyMedins = GroupMeasureCode("mean-of-median")
    """
    Aggregated using Median of study mean values.
    """
    MedianOfStudyMeans = GroupMeasureCode("median-of-mean")
    """
    Aggregated using Median of study median values.
    """
    MedianOfStudyMedians = GroupMeasureCode("median-of-median")
