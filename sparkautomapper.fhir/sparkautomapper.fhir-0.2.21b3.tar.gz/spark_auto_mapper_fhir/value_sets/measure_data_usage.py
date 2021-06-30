from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MeasureDataUsageCode(FhirValueSetBase):
    """
    MeasureDataUsage
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/measure-data-usage
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/measure-data-usage"


class MeasureDataUsageCodeValues:
    """
    The data is intended to be provided as additional information alongside the measure results.
    """

    SupplementalData = MeasureDataUsageCode("supplemental-data")
    """
    The data is intended to be used to calculate and apply a risk adjustment model for the measure.
    """
    RiskAdjustmentFactor = MeasureDataUsageCode("risk-adjustment-factor")
