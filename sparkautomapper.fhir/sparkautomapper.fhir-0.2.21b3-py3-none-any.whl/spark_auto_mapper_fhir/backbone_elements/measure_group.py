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
    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for code
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for code
    # description (string)
    # population (Measure.Population)
    from spark_auto_mapper_fhir.backbone_elements.measure_population import (
        MeasurePopulation,
    )

    # stratifier (Measure.Stratifier)
    from spark_auto_mapper_fhir.backbone_elements.measure_stratifier import (
        MeasureStratifier,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MeasureGroup(FhirBackboneElementBase):
    """
    Measure.Group
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        code: Optional[CodeableConcept[GenericTypeCode]] = None,
        description: Optional[FhirString] = None,
        population: Optional[FhirList[MeasurePopulation]] = None,
        stratifier: Optional[FhirList[MeasureStratifier]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param code: Indicates a meaning for the group. This can be as simple as a unique
        identifier, or it can establish meaning in a broader context by drawing from a
        terminology, allowing groups to be correlated across measures.
            :param description: The human readable description of this population group.
            :param population: A population criteria for the measure.
            :param stratifier: The stratifier criteria for the measure report, specified as either the name
        of a valid CQL expression defined within a referenced library or a valid FHIR
        Resource Path.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            description=description,
            population=population,
            stratifier=stratifier,
        )
