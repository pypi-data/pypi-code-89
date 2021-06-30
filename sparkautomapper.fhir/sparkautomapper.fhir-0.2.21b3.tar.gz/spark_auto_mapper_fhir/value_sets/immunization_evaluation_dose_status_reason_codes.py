from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ImmunizationEvaluationDoseStatusReasonCodesCode(FhirValueSetBase):
    """
    ImmunizationEvaluationDoseStatusReasonCodes
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/immunization-evaluation-dose-status-reason
    """
    codeset: FhirUri = (
        "http://hl7.org/fhir/ValueSet/immunization-evaluation-dose-status-reason"
    )


class ImmunizationEvaluationDoseStatusReasonCodesCodeValues:
    """
    The product was stored in a manner inconsistent with manufacturer guidelines potentially reducing the effectiveness of the product.
    """

    AdverseStorageCondition = ImmunizationEvaluationDoseStatusReasonCodesCode(
        "advstorage"
    )
    """
    The product was stored at a temperature inconsistent with manufacturer guidelines potentially reducing the effectiveness of the product.
    """
    ColdChainBreak = ImmunizationEvaluationDoseStatusReasonCodesCode("coldchbrk")
    """
    The product was administered after the expiration date associated with lot of vaccine.
    """
    ExpiredLot = ImmunizationEvaluationDoseStatusReasonCodesCode("explot")
    """
    The product was administered at a time inconsistent with the documented schedule.
    """
    AdministeredOutsideRecommendedSchedule = (
        ImmunizationEvaluationDoseStatusReasonCodesCode("outsidesched")
    )
    """
    The product administered has been recalled by the manufacturer.
    """
    ProductRecall = ImmunizationEvaluationDoseStatusReasonCodesCode("prodrecall")
