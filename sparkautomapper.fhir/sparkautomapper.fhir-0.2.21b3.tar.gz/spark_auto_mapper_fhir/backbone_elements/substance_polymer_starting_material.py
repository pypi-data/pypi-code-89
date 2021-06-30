from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # material (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for material
    # Import for CodeableConcept for material
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for material
    # type_ (CodeableConcept)
    # End Import for References for type_
    # Import for CodeableConcept for type_
    # End Import for CodeableConcept for type_
    # isDefining (boolean)
    # amount (SubstanceAmount)
    from spark_auto_mapper_fhir.backbone_elements.substance_amount import (
        SubstanceAmount,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstancePolymerStartingMaterial(FhirBackboneElementBase):
    """
    SubstancePolymer.StartingMaterial
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        material: Optional[CodeableConcept[GenericTypeCode]] = None,
        type_: Optional[CodeableConcept[GenericTypeCode]] = None,
        isDefining: Optional[FhirBoolean] = None,
        amount: Optional[SubstanceAmount] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param material: Todo.
        :param type_: Todo.
        :param isDefining: Todo.
        :param amount: Todo.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            material=material,
            type_=type_,
            isDefining=isDefining,
            amount=amount,
        )
