from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # description (string)
    # numberOfStudies (integer)
    # numberOfParticipants (integer)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RiskEvidenceSynthesisSampleSize(FhirBackboneElementBase):
    """
    RiskEvidenceSynthesis.SampleSize
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        description: Optional[FhirString] = None,
        numberOfStudies: Optional[FhirInteger] = None,
        numberOfParticipants: Optional[FhirInteger] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param description: Human-readable summary of sample size.
        :param numberOfStudies: Number of studies included in this evidence synthesis.
        :param numberOfParticipants: Number of participants included in this evidence synthesis.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            description=description,
            numberOfStudies=numberOfStudies,
            numberOfParticipants=numberOfParticipants,
        )
