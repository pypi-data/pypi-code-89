from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # description (string)
    # timeDateTime (dateTime)
    # timePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class BiologicallyDerivedProductManipulation(FhirBackboneElementBase):
    """
    BiologicallyDerivedProduct.Manipulation
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        description: Optional[FhirString] = None,
        timeDateTime: Optional[FhirDateTime] = None,
        timePeriod: Optional[Period] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param description: Description of manipulation.
        :param timeDateTime: None
        :param timePeriod: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            description=description,
            timeDateTime=timeDateTime,
            timePeriod=timePeriod,
        )
