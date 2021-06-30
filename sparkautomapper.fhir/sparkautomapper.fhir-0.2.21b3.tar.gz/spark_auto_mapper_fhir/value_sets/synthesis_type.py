from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SynthesisTypeCode(FhirValueSetBase):
    """
    SynthesisType
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/synthesis-type
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/synthesis-type"


class SynthesisTypeCodeValues:
    """
    A meta-analysis of the summary data of estimates from individual studies or data sets.
    """

    SummaryDataMeta_analysis = SynthesisTypeCode("std-MA")
    """
    A meta-analysis of the individual participant data from individual studies or data sets.
    """
    IndividualPatientDataMeta_analysis = SynthesisTypeCode("IPD-MA")
    """
    An indirect meta-analysis derived from 2 or more direct comparisons in a network meta-analysis.
    """
    IndirectNetworkMeta_analysis = SynthesisTypeCode("indirect-NMA")
    """
    An composite meta-analysis derived from direct comparisons and indirect comparisons in a network meta-analysis.
    """
    CombinedDirectPlusIndirectNetworkMeta_analysis = SynthesisTypeCode("combined-NMA")
    """
    A range of results across a body of evidence.
    """
    RangeOfResults = SynthesisTypeCode("range")
    """
    An approach describing a body of evidence by categorically classifying individual studies (eg 3 studies showed beneft and 2 studied found no effect).
    """
    ClassifcationOfResults = SynthesisTypeCode("classification")
