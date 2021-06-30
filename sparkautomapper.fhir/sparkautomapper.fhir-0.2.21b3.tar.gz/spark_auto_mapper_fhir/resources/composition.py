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

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.composition import CompositionSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # status (CompositionStatus)
    from spark_auto_mapper_fhir.value_sets.composition_status import (
        CompositionStatusCode,
    )

    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.fhir_document_type_codes import (
        FHIRDocumentTypeCodesCode,
    )

    # End Import for CodeableConcept for type_
    # category (CodeableConcept)
    # Import for CodeableConcept for category
    from spark_auto_mapper_fhir.value_sets.document_class_value_set import (
        DocumentClassValueSetCode,
    )

    # End Import for CodeableConcept for category
    # subject (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.resource import Resource

    # encounter (Reference)
    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # date (dateTime)
    # author (Reference)
    # Imports for References for author
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.organization import Organization

    # title (string)
    # confidentiality (ConfidentialityClassification)
    from spark_auto_mapper_fhir.value_sets.confidentiality_classification import (
        ConfidentialityClassification,
    )

    # attester (Composition.Attester)
    from spark_auto_mapper_fhir.backbone_elements.composition_attester import (
        CompositionAttester,
    )

    # custodian (Reference)
    # Imports for References for custodian
    # relatesTo (Composition.RelatesTo)
    from spark_auto_mapper_fhir.backbone_elements.composition_relates_to import (
        CompositionRelatesTo,
    )

    # event (Composition.Event)
    from spark_auto_mapper_fhir.backbone_elements.composition_event import (
        CompositionEvent,
    )

    # section (Composition.Section)
    from spark_auto_mapper_fhir.backbone_elements.composition_section import (
        CompositionSection,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Composition(FhirResourceBase):
    """
    Composition
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[Identifier] = None,
        status: CompositionStatusCode,
        type_: CodeableConcept[FHIRDocumentTypeCodesCode],
        category: Optional[FhirList[CodeableConcept[DocumentClassValueSetCode]]] = None,
        subject: Optional[Reference[Union[Resource]]] = None,
        encounter: Optional[Reference[Union[Encounter]]] = None,
        date: FhirDateTime,
        author: FhirList[
            Reference[
                Union[
                    Practitioner,
                    PractitionerRole,
                    Device,
                    Patient,
                    RelatedPerson,
                    Organization,
                ]
            ]
        ],
        title: FhirString,
        confidentiality: Optional[ConfidentialityClassification] = None,
        attester: Optional[FhirList[CompositionAttester]] = None,
        custodian: Optional[Reference[Union[Organization]]] = None,
        relatesTo: Optional[FhirList[CompositionRelatesTo]] = None,
        event: Optional[FhirList[CompositionEvent]] = None,
        section: Optional[FhirList[CompositionSection]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: A version-independent identifier for the Composition. This identifier stays
        constant as the composition is changed over time.
            :param status: The workflow/clinical status of this composition. The status is a marker for
        the clinical standing of the document.
            :param type_: Specifies the particular kind of composition (e.g. History and Physical,
        Discharge Summary, Progress Note). This usually equates to the purpose of
        making the composition.
            :param category: A categorization for the type of the composition - helps for indexing and
        searching. This may be implied by or derived from the code specified in the
        Composition Type.
            :param subject: Who or what the composition is about. The composition can be about a person,
        (patient or healthcare practitioner), a device (e.g. a machine) or even a
        group of subjects (such as a document about a herd of livestock, or a set of
        patients that share a common exposure).
            :param encounter: Describes the clinical encounter or type of care this documentation is
        associated with.
            :param date: The composition editing time, when the composition was last logically changed
        by the author.
            :param author: Identifies who is responsible for the information in the composition, not
        necessarily who typed it in.
            :param title: Official human-readable label for the composition.
            :param confidentiality: The code specifying the level of confidentiality of the Composition.
            :param attester: A participant who has attested to the accuracy of the composition/document.
            :param custodian: Identifies the organization or group who is responsible for ongoing
        maintenance of and access to the composition/document information.
            :param relatesTo: Relationships that this composition has with other compositions or documents
        that already exist.
            :param event: The clinical service, such as a colonoscopy or an appendectomy, being
        documented.
            :param section: The root of the sections that make up the composition.
        """
        super().__init__(
            resourceType="Composition",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            type_=type_,
            category=category,
            subject=subject,
            encounter=encounter,
            date=date,
            author=author,
            title=title,
            confidentiality=confidentiality,
            attester=attester,
            custodian=custodian,
            relatesTo=relatesTo,
            event=event,
            section=section,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return CompositionSchema.get_schema(include_extension=include_extension)
