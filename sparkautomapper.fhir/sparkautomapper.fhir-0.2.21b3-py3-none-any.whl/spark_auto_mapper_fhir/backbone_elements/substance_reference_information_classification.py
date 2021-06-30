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
    # domain (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for domain
    # Import for CodeableConcept for domain
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for domain
    # classification (CodeableConcept)
    # End Import for References for classification
    # Import for CodeableConcept for classification
    # End Import for CodeableConcept for classification
    # subtype (CodeableConcept)
    # End Import for References for subtype
    # Import for CodeableConcept for subtype
    # End Import for CodeableConcept for subtype
    # source (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for source
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceReferenceInformationClassification(FhirBackboneElementBase):
    """
    SubstanceReferenceInformation.Classification
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        domain: Optional[CodeableConcept[GenericTypeCode]] = None,
        classification: Optional[CodeableConcept[GenericTypeCode]] = None,
        subtype: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        source: Optional[FhirList[Reference[Union[DocumentReference]]]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param domain: Todo.
        :param classification: Todo.
        :param subtype: Todo.
        :param source: Todo.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            domain=domain,
            classification=classification,
            subtype=subtype,
            source=source,
        )
