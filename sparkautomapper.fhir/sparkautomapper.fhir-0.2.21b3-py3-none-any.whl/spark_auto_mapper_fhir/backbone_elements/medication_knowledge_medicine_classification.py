from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for type_
    # classification (CodeableConcept)
    # End Import for References for classification
    # Import for CodeableConcept for classification
    # End Import for CodeableConcept for classification


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationKnowledgeMedicineClassification(FhirBackboneElementBase):
    """
    MedicationKnowledge.MedicineClassification
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type_: CodeableConcept[GenericTypeCode],
        classification: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param type_: The type of category for the medication (for example, therapeutic
        classification, therapeutic sub-classification).
            :param classification: Specific category assigned to the medication (e.g. anti-infective, anti-
        hypertensive, antibiotic, etc.).
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            classification=classification,
        )
