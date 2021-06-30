from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for type_
    # source (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for source
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference
    from spark_auto_mapper_fhir.resources.media import Media


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationKnowledgeMonograph(FhirBackboneElementBase):
    """
    MedicationKnowledge.Monograph
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type_: Optional[CodeableConcept[GenericTypeCode]] = None,
        source: Optional[Reference[Union[DocumentReference, Media]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param type_: The category of documentation about the medication. (e.g. professional
        monograph, patient education monograph).
            :param source: Associated documentation about the medication.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            source=source,
        )
