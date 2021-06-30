from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.researchsubject import ResearchSubjectSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # status (ResearchSubjectStatus)
    from spark_auto_mapper_fhir.value_sets.research_subject_status import (
        ResearchSubjectStatusCode,
    )

    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # study (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for study
    from spark_auto_mapper_fhir.resources.research_study import ResearchStudy

    # individual (Reference)
    # Imports for References for individual
    from spark_auto_mapper_fhir.resources.patient import Patient

    # assignedArm (string)
    # actualArm (string)
    # consent (Reference)
    # Imports for References for consent
    from spark_auto_mapper_fhir.resources.consent import Consent


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ResearchSubject(FhirResourceBase):
    """
    ResearchSubject
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: ResearchSubjectStatusCode,
        period: Optional[Period] = None,
        study: Reference[Union[ResearchStudy]],
        individual: Reference[Union[Patient]],
        assignedArm: Optional[FhirString] = None,
        actualArm: Optional[FhirString] = None,
        consent: Optional[Reference[Union[Consent]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Identifiers assigned to this research subject for a study.
            :param status: The current state of the subject.
            :param period: The dates the subject began and ended their participation in the study.
            :param study: Reference to the study the subject is participating in.
            :param individual: The record of the person or animal who is involved in the study.
            :param assignedArm: The name of the arm in the study the subject is expected to follow as part of
        this study.
            :param actualArm: The name of the arm in the study the subject actually followed as part of this
        study.
            :param consent: A record of the patient's informed agreement to participate in the study.
        """
        super().__init__(
            resourceType="ResearchSubject",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            period=period,
            study=study,
            individual=individual,
            assignedArm=assignedArm,
            actualArm=actualArm,
            consent=consent,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ResearchSubjectSchema.get_schema(include_extension=include_extension)
