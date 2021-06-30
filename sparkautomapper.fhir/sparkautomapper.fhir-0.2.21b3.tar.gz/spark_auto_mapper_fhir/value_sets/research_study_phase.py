from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ResearchStudyPhaseCode(FhirValueSetBase):
    """
    ResearchStudyPhase
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/research-study-phase
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/research-study-phase"


class ResearchStudyPhaseCodeValues:
    """
    Trials without phases (for example, studies of devices or behavioral interventions).
    """

    N_A = ResearchStudyPhaseCode("n-a")
    """
    Designation for optional exploratory trials conducted in accordance with the United States Food and Drug Administration's (FDA) 2006 Guidance on Exploratory Investigational New Drug (IND) Studies. Formerly called Phase 0.
    """
    EarlyPhase1 = ResearchStudyPhaseCode("early-phase-1")
    """
    Includes initial studies to determine the metabolism and pharmacologic actions of drugs in humans, the side effects associated with increasing doses, and to gain early evidence of effectiveness; may include healthy participants and/or patients.
    """
    Phase1 = ResearchStudyPhaseCode("phase-1")
    """
    Trials that are a combination of phases 1 and 2.
    """
    Phase1_Phase2 = ResearchStudyPhaseCode("phase-1-phase-2")
    """
    Includes controlled clinical studies conducted to evaluate the effectiveness of the drug for a particular indication or indications in participants with the disease or condition under study and to determine the common short-term side effects and risks.
    """
    Phase2 = ResearchStudyPhaseCode("phase-2")
    """
    Trials that are a combination of phases 2 and 3.
    """
    Phase2_Phase3 = ResearchStudyPhaseCode("phase-2-phase-3")
    """
    Includes trials conducted after preliminary evidence suggesting effectiveness of the drug has been obtained, and are intended to gather additional information to evaluate the overall benefit-risk relationship of the drug.
    """
    Phase3 = ResearchStudyPhaseCode("phase-3")
    """
    Studies of FDA-approved drugs to delineate additional information including the drug's risks, benefits, and optimal use.
    """
    Phase4 = ResearchStudyPhaseCode("phase-4")
