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
    # criteria (Expression)
    from spark_auto_mapper_fhir.complex_types.expression import Expression


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MeasureComponent(FhirBackboneElementBase):
    """
    Measure.Component
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        code: Optional[CodeableConcept[GenericTypeCode]] = None,
        description: Optional[FhirString] = None,
        criteria: Expression,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param code: Indicates a meaning for the stratifier component. This can be as simple as a
        unique identifier, or it can establish meaning in a broader context by drawing
        from a terminology, allowing stratifiers to be correlated across measures.
            :param description: The human readable description of this stratifier criteria component.
            :param criteria: An expression that specifies the criteria for this component of the
        stratifier. This is typically the name of an expression defined within a
        referenced library, but it may also be a path to a stratifier element.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            description=description,
            criteria=criteria,
        )
