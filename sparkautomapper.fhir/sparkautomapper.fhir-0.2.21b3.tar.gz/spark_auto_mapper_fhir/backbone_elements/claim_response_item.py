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
    # itemSequence (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # noteNumber (positiveInt)
    # adjudication (ClaimResponse.Adjudication)
    from spark_auto_mapper_fhir.backbone_elements.claim_response_adjudication import (
        ClaimResponseAdjudication,
    )

    # detail (ClaimResponse.Detail)
    from spark_auto_mapper_fhir.backbone_elements.claim_response_detail import (
        ClaimResponseDetail,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ClaimResponseItem(FhirBackboneElementBase):
    """
    ClaimResponse.Item
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        itemSequence: FhirPositiveInt,
        noteNumber: Optional[FhirList[FhirPositiveInt]] = None,
        adjudication: FhirList[ClaimResponseAdjudication],
        detail: Optional[FhirList[ClaimResponseDetail]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param itemSequence: A number to uniquely reference the claim item entries.
            :param noteNumber: The numbers associated with notes below which apply to the adjudication of
        this item.
            :param adjudication: If this item is a group then the values here are a summary of the adjudication
        of the detail items. If this item is a simple product or service then this is
        the result of the adjudication of this item.
            :param detail: A claim detail. Either a simple (a product or service) or a 'group' of sub-
        details which are simple items.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            itemSequence=itemSequence,
            noteNumber=noteNumber,
            adjudication=adjudication,
            detail=detail,
        )
