from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # fraction (string)
    # materialType (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for materialType
    # Import for CodeableConcept for materialType
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for materialType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceSourceMaterialFractionDescription(FhirBackboneElementBase):
    """
    SubstanceSourceMaterial.FractionDescription
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        fraction: Optional[FhirString] = None,
        materialType: Optional[CodeableConcept[GenericTypeCode]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param fraction: This element is capturing information about the fraction of a plant part, or
        human plasma for fractionation.
            :param materialType: The specific type of the material constituting the component. For Herbal
        preparations the particulars of the extracts (liquid/dry) is described in
        Specified Substance Group 1.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            fraction=fraction,
            materialType=materialType,
        )
