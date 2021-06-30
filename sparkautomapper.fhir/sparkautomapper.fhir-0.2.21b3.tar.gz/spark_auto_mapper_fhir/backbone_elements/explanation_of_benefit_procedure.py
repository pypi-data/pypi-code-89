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
    # sequence (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.example_procedure_type_codes import (
        ExampleProcedureTypeCodesCode,
    )

    # End Import for CodeableConcept for type_
    # date (dateTime)
    # udi (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for udi
    from spark_auto_mapper_fhir.resources.device import Device

    # procedureCodeableConcept (CodeableConcept)
    # End Import for References for procedureCodeableConcept
    # Import for CodeableConcept for procedureCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for procedureCodeableConcept
    # procedureReference (Reference)
    # Imports for References for procedureReference
    from spark_auto_mapper_fhir.resources.procedure import Procedure


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ExplanationOfBenefitProcedure(FhirBackboneElementBase):
    """
    ExplanationOfBenefit.Procedure
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        sequence: FhirPositiveInt,
        type_: Optional[
            FhirList[CodeableConcept[ExampleProcedureTypeCodesCode]]
        ] = None,
        date: Optional[FhirDateTime] = None,
        udi: Optional[FhirList[Reference[Union[Device]]]] = None,
        procedureCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        procedureReference: Optional[Reference[Union[Procedure]]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param sequence: A number to uniquely identify procedure entries.
        :param type_: When the condition was observed or the relative ranking.
        :param date: Date and optionally time the procedure was performed.
        :param udi: Unique Device Identifiers associated with this line item.
        :param procedureCodeableConcept: None
        :param procedureReference: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            sequence=sequence,
            type_=type_,
            date=date,
            udi=udi,
            procedureCodeableConcept=procedureCodeableConcept,
            procedureReference=procedureReference,
        )
