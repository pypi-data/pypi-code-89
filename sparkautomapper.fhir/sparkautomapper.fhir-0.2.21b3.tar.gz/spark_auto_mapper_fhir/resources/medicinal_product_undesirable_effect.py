from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.medicinalproductundesirableeffect import (
    MedicinalProductUndesirableEffectSchema,
)

if TYPE_CHECKING:
    pass
    # subject (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.medicinal_product import MedicinalProduct
    from spark_auto_mapper_fhir.resources.medication import Medication

    # symptomConditionEffect (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for symptomConditionEffect
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for symptomConditionEffect
    # classification (CodeableConcept)
    # Import for CodeableConcept for classification
    # End Import for CodeableConcept for classification
    # frequencyOfOccurrence (CodeableConcept)
    # Import for CodeableConcept for frequencyOfOccurrence
    # End Import for CodeableConcept for frequencyOfOccurrence
    # population (Population)
    from spark_auto_mapper_fhir.backbone_elements.population import Population


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicinalProductUndesirableEffect(FhirResourceBase):
    """
    MedicinalProductUndesirableEffect
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        subject: Optional[
            FhirList[Reference[Union[MedicinalProduct, Medication]]]
        ] = None,
        symptomConditionEffect: Optional[CodeableConcept[GenericTypeCode]] = None,
        classification: Optional[CodeableConcept[GenericTypeCode]] = None,
        frequencyOfOccurrence: Optional[CodeableConcept[GenericTypeCode]] = None,
        population: Optional[FhirList[Population]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param meta: Meta
        :param extension: extensions
        :param subject: The medication for which this is an indication.
        :param symptomConditionEffect: The symptom, condition or undesirable effect.
        :param classification: Classification of the effect.
        :param frequencyOfOccurrence: The frequency of occurrence of the effect.
        :param population: The population group to which this applies.
        """
        super().__init__(
            resourceType="MedicinalProductUndesirableEffect",
            id_=id_,
            meta=meta,
            extension=extension,
            subject=subject,
            symptomConditionEffect=symptomConditionEffect,
            classification=classification,
            frequencyOfOccurrence=frequencyOfOccurrence,
            population=population,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MedicinalProductUndesirableEffectSchema.get_schema(
            include_extension=include_extension
        )
