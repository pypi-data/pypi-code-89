from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # action (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for action
    # Import for CodeableConcept for action
    from spark_auto_mapper_fhir.value_sets.detected_issue_mitigation_action import (
        DetectedIssueMitigationActionCode,
    )

    # End Import for CodeableConcept for action
    # date (dateTime)
    # author (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for author
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DetectedIssueMitigation(FhirBackboneElementBase):
    """
    DetectedIssue.Mitigation
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        action: CodeableConcept[DetectedIssueMitigationActionCode],
        date: Optional[FhirDateTime] = None,
        author: Optional[Reference[Union[Practitioner, PractitionerRole]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param action: Describes the action that was taken or the observation that was made that
        reduces/eliminates the risk associated with the identified issue.
            :param date: Indicates when the mitigating action was documented.
            :param author: Identifies the practitioner who determined the mitigation and takes
        responsibility for the mitigation step occurring.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            action=action,
            date=date,
            author=author,
        )
