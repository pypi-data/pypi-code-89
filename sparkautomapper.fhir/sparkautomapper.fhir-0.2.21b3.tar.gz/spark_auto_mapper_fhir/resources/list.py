from __future__ import annotations

from typing import Optional, Union, TYPE_CHECKING

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.list import ListSchema

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString

if TYPE_CHECKING:
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # status (ListStatus)
    from spark_auto_mapper_fhir.value_sets.list_status import ListStatusCode

    # mode (ListMode)
    from spark_auto_mapper_fhir.value_sets.list_mode import ListModeCode

    # title (string)

    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.example_use_codes_for_list import (
        ExampleUseCodesForListCode,
    )

    # End Import for CodeableConcept for code
    # subject (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for subject
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.location import Location

    # encounter (Reference)

    # Imports for References for encounter
    from spark_auto_mapper_fhir.resources.encounter import Encounter

    # date (dateTime)

    # source (Reference)

    # Imports for References for source
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # orderedBy (CodeableConcept)

    # Import for CodeableConcept for orderedBy
    from spark_auto_mapper_fhir.value_sets.list_order_codes import ListOrderCodesCode

    # End Import for CodeableConcept for orderedBy
    # note (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # entry (List.Entry)
    from spark_auto_mapper_fhir.backbone_elements.list_entry import ListEntry

    # emptyReason (CodeableConcept)

    # Import for CodeableConcept for emptyReason
    from spark_auto_mapper_fhir.value_sets.list_empty_reasons import (
        ListEmptyReasonsCode,
    )

    # End Import for CodeableConcept for emptyReason


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class List_(FhirResourceBase):
    """
    List
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: ListStatusCode,
        mode: ListModeCode,
        title: Optional[FhirString] = None,
        code: Optional[CodeableConcept[ExampleUseCodesForListCode]] = None,
        subject: Optional[Reference[Union[Patient, Group, Device, Location]]] = None,
        encounter: Optional[Reference[Union[Encounter]]] = None,
        date: Optional[FhirDateTime] = None,
        source: Optional[
            Reference[Union[Practitioner, PractitionerRole, Patient, Device]]
        ] = None,
        orderedBy: Optional[CodeableConcept[ListOrderCodesCode]] = None,
        note: Optional[FhirList[Annotation]] = None,
        entry: Optional[FhirList[ListEntry]] = None,
        emptyReason: Optional[CodeableConcept[ListEmptyReasonsCode]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: Identifier for the List assigned for business purposes outside the context of
        FHIR.
            :param status: Indicates the current state of this list.
            :param mode: How this list was prepared - whether it is a working list that is suitable for
        being maintained on an ongoing basis, or if it represents a snapshot of a list
        of items from another source, or whether it is a prepared list where items may
        be marked as added, modified or deleted.
            :param title: A label for the list assigned by the author.
            :param code: This code defines the purpose of the list - why it was created.
            :param subject: The common subject (or patient) of the resources that are in the list if there
        is one.
            :param encounter: The encounter that is the context in which this list was created.
            :param date: The date that the list was prepared.
            :param source: The entity responsible for deciding what the contents of the list were. Where
        the list was created by a human, this is the same as the author of the list.
            :param orderedBy: What order applies to the items in the list.
            :param note: Comments that apply to the overall list.
            :param entry: Entries in this list.
            :param emptyReason: If the list is empty, why the list is empty.
        """
        super().__init__(
            resourceType="List_",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            mode=mode,
            title=title,
            code=code,
            subject=subject,
            encounter=encounter,
            date=date,
            source=source,
            orderedBy=orderedBy,
            note=note,
            entry=entry,
            emptyReason=emptyReason,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ListSchema.get_schema(include_extension=include_extension)
