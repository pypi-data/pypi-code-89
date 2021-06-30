from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

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
    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for code
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for code
    # status (CodeableConcept)
    # End Import for References for status
    # Import for CodeableConcept for status
    # End Import for CodeableConcept for status
    # statusDate (dateTime)
    # comment (string)
    # source (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for source
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceSpecificationCode(FhirBackboneElementBase):
    """
    SubstanceSpecification.Code
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        code: Optional[CodeableConcept[GenericTypeCode]] = None,
        status: Optional[CodeableConcept[GenericTypeCode]] = None,
        statusDate: Optional[FhirDateTime] = None,
        comment: Optional[FhirString] = None,
        source: Optional[FhirList[Reference[Union[DocumentReference]]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param code: The specific code.
            :param status: Status of the code assignment.
            :param statusDate: The date at which the code status is changed as part of the terminology
        maintenance.
            :param comment: Any comment can be provided in this field, if necessary.
            :param source: Supporting literature.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            status=status,
            statusDate=statusDate,
            comment=comment,
            source=source,
        )
