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
    # part (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for part
    # Import for CodeableConcept for part
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for part
    # partLocation (CodeableConcept)
    # End Import for References for partLocation
    # Import for CodeableConcept for partLocation
    # End Import for CodeableConcept for partLocation


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceSourceMaterialPartDescription(FhirBackboneElementBase):
    """
    SubstanceSourceMaterial.PartDescription
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        part: Optional[CodeableConcept[GenericTypeCode]] = None,
        partLocation: Optional[CodeableConcept[GenericTypeCode]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param part: Entity of anatomical origin of source material within an organism.
            :param partLocation: The detailed anatomic location when the part can be extracted from different
        anatomical locations of the organism. Multiple alternative locations may
        apply.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            part=part,
            partLocation=partLocation,
        )
