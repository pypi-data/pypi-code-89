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
    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # duration (Duration)
    from spark_auto_mapper_fhir.complex_types.duration import Duration


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationRequestInitialFill(FhirBackboneElementBase):
    """
    MedicationRequest.InitialFill
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        quantity: Optional[Quantity] = None,
        duration: Optional[Duration] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param quantity: The amount or quantity to provide as part of the first dispense.
        :param duration: The length of time that the first dispense is expected to last.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            quantity=quantity,
            duration=duration,
        )
