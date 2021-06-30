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
    # status (EncounterStatus)
    from spark_auto_mapper_fhir.value_sets.encounter_status import EncounterStatusCode

    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EncounterStatusHistory(FhirBackboneElementBase):
    """
    Encounter.StatusHistory
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        status: EncounterStatusCode,
        period: Period,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param status: planned | arrived | triaged | in-progress | onleave | finished | cancelled +.
        :param period: The time that the episode was in the specified status.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            status=status,
            period=period,
        )
