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
    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for code
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for code
    # status (CodeableConcept)
    # End Import for References for status
    # Import for CodeableConcept for status
    # End Import for CodeableConcept for status


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicinalProductPharmaceuticalCharacteristics(FhirBackboneElementBase):
    """
    MedicinalProductPharmaceutical.Characteristics
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        code: CodeableConcept[GenericTypeCode],
        status: Optional[CodeableConcept[GenericTypeCode]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param code: A coded characteristic.
        :param status: The status of characteristic e.g. assigned or pending.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            status=status,
        )
