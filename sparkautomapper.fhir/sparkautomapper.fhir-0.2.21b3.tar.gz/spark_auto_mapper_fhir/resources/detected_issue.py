from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.detectedissue import DetectedIssueSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # status (ObservationStatus)
    from spark_auto_mapper_fhir.value_sets.observation_status import (
        ObservationStatusCode,
    )

    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.detected_issue_category import (
        DetectedIssueCategoryCode,
    )

    # End Import for CodeableConcept for code
    # severity (DetectedIssueSeverity)
    from spark_auto_mapper_fhir.value_sets.detected_issue_severity import (
        DetectedIssueSeverityCode,
    )

    # patient (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for patient
    from spark_auto_mapper_fhir.resources.patient import Patient

    # author (Reference)
    # Imports for References for author
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.device import Device

    # implicated (Reference)
    # Imports for References for implicated
    from spark_auto_mapper_fhir.resources.resource import Resource

    # evidence (DetectedIssue.Evidence)
    from spark_auto_mapper_fhir.backbone_elements.detected_issue_evidence import (
        DetectedIssueEvidence,
    )

    # detail (string)
    # reference (uri)
    # mitigation (DetectedIssue.Mitigation)
    from spark_auto_mapper_fhir.backbone_elements.detected_issue_mitigation import (
        DetectedIssueMitigation,
    )

    # identifiedDateTime (dateTime)
    # identifiedPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DetectedIssue(FhirResourceBase):
    """
    DetectedIssue
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: ObservationStatusCode,
        code: Optional[CodeableConcept[DetectedIssueCategoryCode]] = None,
        severity: Optional[DetectedIssueSeverityCode] = None,
        patient: Optional[Reference[Union[Patient]]] = None,
        author: Optional[
            Reference[Union[Practitioner, PractitionerRole, Device]]
        ] = None,
        implicated: Optional[FhirList[Reference[Union[Resource]]]] = None,
        evidence: Optional[FhirList[DetectedIssueEvidence]] = None,
        detail: Optional[FhirString] = None,
        reference: Optional[FhirUri] = None,
        mitigation: Optional[FhirList[DetectedIssueMitigation]] = None,
        identifiedDateTime: Optional[FhirDateTime] = None,
        identifiedPeriod: Optional[Period] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Business identifier associated with the detected issue record.
            :param status: Indicates the status of the detected issue.
            :param code: Identifies the general type of issue identified.
            :param severity: Indicates the degree of importance associated with the identified issue based
        on the potential impact on the patient.
            :param patient: Indicates the patient whose record the detected issue is associated with.
            :param author: Individual or device responsible for the issue being raised.  For example, a
        decision support application or a pharmacist conducting a medication review.
            :param implicated: Indicates the resource representing the current activity or proposed activity
        that is potentially problematic.
            :param evidence: Supporting evidence or manifestations that provide the basis for identifying
        the detected issue such as a GuidanceResponse or MeasureReport.
            :param detail: A textual explanation of the detected issue.
            :param reference: The literature, knowledge-base or similar reference that describes the
        propensity for the detected issue identified.
            :param mitigation: Indicates an action that has been taken or is committed to reduce or eliminate
        the likelihood of the risk identified by the detected issue from manifesting.
        Can also reflect an observation of known mitigating factors that may
        reduce/eliminate the need for any action.
            :param identifiedDateTime: None
            :param identifiedPeriod: None
        """
        super().__init__(
            resourceType="DetectedIssue",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            code=code,
            severity=severity,
            patient=patient,
            author=author,
            implicated=implicated,
            evidence=evidence,
            detail=detail,
            reference=reference,
            mitigation=mitigation,
            identifiedDateTime=identifiedDateTime,
            identifiedPeriod=identifiedPeriod,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return DetectedIssueSchema.get_schema(include_extension=include_extension)
