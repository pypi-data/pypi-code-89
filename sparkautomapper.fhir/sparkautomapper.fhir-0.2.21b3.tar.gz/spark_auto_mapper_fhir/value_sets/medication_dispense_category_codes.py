from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationDispenseCategoryCodesCode(FhirValueSetBase):
    """
    MedicationDispense Category Codes
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/medicationdispense-category
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/medicationdispense-category"


class MedicationDispenseCategoryCodesCodeValues:
    """
    Includes dispenses for medications to be administered or consumed in an inpatient or acute care setting.
    """

    Inpatient = MedicationDispenseCategoryCodesCode("inpatient")
    """
    Includes dispenses for medications to be administered or consumed in an outpatient setting (for example, Emergency Department, Outpatient Clinic, Outpatient Surgery, Doctor's office).
    """
    Outpatient = MedicationDispenseCategoryCodesCode("outpatient")
    """
    Includes dispenses for medications to be administered or consumed by the patient in their home (this would include long term care or nursing homes, hospices, etc.).
    """
    Community = MedicationDispenseCategoryCodesCode("community")
    """
    Includes dispenses for medications created when the patient is being released from a facility.
    """
    Discharge = MedicationDispenseCategoryCodesCode("discharge")
