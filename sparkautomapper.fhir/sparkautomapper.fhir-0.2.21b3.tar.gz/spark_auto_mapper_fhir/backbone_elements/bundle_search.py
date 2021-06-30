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
    # mode (SearchEntryMode)
    from spark_auto_mapper_fhir.value_sets.search_entry_mode import SearchEntryModeCode

    # score (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class BundleSearch(FhirBackboneElementBase):
    """
    Bundle.Search
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        mode: Optional[SearchEntryModeCode] = None,
        score: Optional[FhirDecimal] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param mode: Why this entry is in the result set - whether it's included as a match or
        because of an _include requirement, or to convey information or warning
        information about the search process.
            :param score: When searching, the server's search ranking score for the entry.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            mode=mode,
            score=score,
        )
