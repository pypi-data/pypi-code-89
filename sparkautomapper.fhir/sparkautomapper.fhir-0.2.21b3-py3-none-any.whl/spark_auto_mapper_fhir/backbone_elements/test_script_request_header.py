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
    # field (string)
    # value (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TestScriptRequestHeader(FhirBackboneElementBase):
    """
    TestScript.RequestHeader
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        field: FhirString,
        value: FhirString,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param field: The HTTP header field e.g. "Accept".
        :param value: The value of the header e.g. "application/fhir+xml".
        """
        super().__init__(
            id_=id_,
            extension=extension,
            field=field,
            value=value,
        )
