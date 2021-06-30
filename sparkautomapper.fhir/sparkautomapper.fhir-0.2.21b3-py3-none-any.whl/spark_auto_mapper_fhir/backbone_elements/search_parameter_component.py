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
    # definition (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # expression (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SearchParameterComponent(FhirBackboneElementBase):
    """
    SearchParameter.Component
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        definition: FhirCanonical,
        expression: FhirString,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param definition: The definition of the search parameter that describes this part.
            :param expression: A sub-expression that defines how to extract values for this component from
        the output of the main SearchParameter.expression.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            definition=definition,
            expression=expression,
        )
