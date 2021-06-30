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
    # translation (boolean)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TerminologyCapabilitiesClosure(FhirBackboneElementBase):
    """
    TerminologyCapabilities.Closure
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        translation: Optional[FhirBoolean] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param translation: If cross-system closure is supported.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            translation=translation,
        )
