from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CertaintySubcomponentTypeCode(FhirValueSetBase):
    """
    CertaintySubcomponentType
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/certainty-subcomponent-type
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/certainty-subcomponent-type"


class CertaintySubcomponentTypeCodeValues:
    """
    methodologic concerns reducing internal validity.
    """

    RiskOfBias = CertaintySubcomponentTypeCode("RiskOfBias")
    """
    concerns that findings are not similar enough to support certainty.
    """
    Inconsistency = CertaintySubcomponentTypeCode("Inconsistency")
    """
    concerns reducing external validity.
    """
    Indirectness = CertaintySubcomponentTypeCode("Indirectness")
    """
    High quality evidence.
    """
    Imprecision = CertaintySubcomponentTypeCode("Imprecision")
    """
    likelihood that what is published misrepresents what is available to publish.
    """
    PublicationBias = CertaintySubcomponentTypeCode("PublicationBias")
    """
    higher certainty due to dose response relationship.
    """
    DoseResponseGradient = CertaintySubcomponentTypeCode("DoseResponseGradient")
    """
    higher certainty due to risk of bias in opposite direction.
    """
    PlausibleConfounding = CertaintySubcomponentTypeCode("PlausibleConfounding")
    """
    higher certainty due to large effect size.
    """
    LargeEffect = CertaintySubcomponentTypeCode("LargeEffect")
