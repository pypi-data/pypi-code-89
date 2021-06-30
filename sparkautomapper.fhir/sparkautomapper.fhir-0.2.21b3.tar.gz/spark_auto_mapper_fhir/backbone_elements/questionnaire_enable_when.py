from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.resource import Resource

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # question (string)
    # operator (QuestionnaireItemOperator)
    from spark_auto_mapper_fhir.value_sets.questionnaire_item_operator import (
        QuestionnaireItemOperatorCode,
    )

    # answerBoolean (boolean)
    # answerDecimal (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

    # answerInteger (integer)
    # answerDate (date)
    # answerDateTime (dateTime)
    # answerTime (time)
    from spark_auto_mapper_fhir.fhir_types.time import FhirTime

    # answerString (string)
    # answerCoding (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # End Import for References for answerCoding
    # Import for CodeableConcept for answerCoding
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for answerCoding
    # answerQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # answerReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for answerReference


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class QuestionnaireEnableWhen(FhirBackboneElementBase):
    """
    Questionnaire.EnableWhen
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        question: FhirString,
        operator: QuestionnaireItemOperatorCode,
        answerBoolean: Optional[FhirBoolean] = None,
        answerDecimal: Optional[FhirDecimal] = None,
        answerInteger: Optional[FhirInteger] = None,
        answerDate: Optional[FhirDate] = None,
        answerDateTime: Optional[FhirDateTime] = None,
        answerTime: Optional[FhirTime] = None,
        answerString: Optional[FhirString] = None,
        answerCoding: Optional[Coding[GenericTypeCode]] = None,
        answerQuantity: Optional[Quantity] = None,
        answerReference: Optional[Reference[Union[Resource]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param question: The linkId for the question whose answer (or lack of answer) governs whether
        this item is enabled.
            :param operator: Specifies the criteria by which the question is enabled.
            :param answerBoolean: None
            :param answerDecimal: None
            :param answerInteger: None
            :param answerDate: None
            :param answerDateTime: None
            :param answerTime: None
            :param answerString: None
            :param answerCoding: None
            :param answerQuantity: None
            :param answerReference: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            question=question,
            operator=operator,
            answerBoolean=answerBoolean,
            answerDecimal=answerDecimal,
            answerInteger=answerInteger,
            answerDate=answerDate,
            answerDateTime=answerDateTime,
            answerTime=answerTime,
            answerString=answerString,
            answerCoding=answerCoding,
            answerQuantity=answerQuantity,
            answerReference=answerReference,
        )
