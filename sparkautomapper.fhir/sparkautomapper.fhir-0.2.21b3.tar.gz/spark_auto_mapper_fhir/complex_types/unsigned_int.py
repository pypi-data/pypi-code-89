from __future__ import annotations
from typing import Optional

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class unsignedInt(FhirComplexTypeBase):
    """
    unsignedInt
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        """
        super().__init__(
            id_=id_,
            extension=extension,
        )
