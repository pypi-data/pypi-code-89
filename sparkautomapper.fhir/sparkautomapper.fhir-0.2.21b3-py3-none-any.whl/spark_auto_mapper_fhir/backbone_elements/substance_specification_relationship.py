from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # relationship (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for relationship
    # Import for CodeableConcept for relationship
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for relationship
    # isDefining (boolean)
    # amountRatioLowLimit (Ratio)
    from spark_auto_mapper_fhir.complex_types.ratio import Ratio

    # amountType (CodeableConcept)
    # End Import for References for amountType
    # Import for CodeableConcept for amountType
    # End Import for CodeableConcept for amountType
    # source (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for source
    from spark_auto_mapper_fhir.resources.document_reference import DocumentReference

    # substanceReference (Reference)
    # Imports for References for substanceReference
    from spark_auto_mapper_fhir.resources.substance_specification import (
        SubstanceSpecification,
    )

    # substanceCodeableConcept (CodeableConcept)
    # End Import for References for substanceCodeableConcept
    # Import for CodeableConcept for substanceCodeableConcept
    # End Import for CodeableConcept for substanceCodeableConcept
    # amountQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # amountRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # amountRatio (Ratio)
    # amountString (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubstanceSpecificationRelationship(FhirBackboneElementBase):
    """
    SubstanceSpecification.Relationship
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        relationship: Optional[CodeableConcept[GenericTypeCode]] = None,
        isDefining: Optional[FhirBoolean] = None,
        amountRatioLowLimit: Optional[Ratio] = None,
        amountType: Optional[CodeableConcept[GenericTypeCode]] = None,
        source: Optional[FhirList[Reference[Union[DocumentReference]]]] = None,
        substanceReference: Optional[Reference[Union[SubstanceSpecification]]] = None,
        substanceCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        amountQuantity: Optional[Quantity] = None,
        amountRange: Optional[Range] = None,
        amountRatio: Optional[Ratio] = None,
        amountString: Optional[FhirString] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param relationship: For example "salt to parent", "active moiety", "starting material".
            :param isDefining: For example where an enzyme strongly bonds with a particular substance, this
        is a defining relationship for that enzyme, out of several possible substance
        relationships.
            :param amountRatioLowLimit: For use when the numeric.
            :param amountType: An operator for the amount, for example "average", "approximately", "less
        than".
            :param source: Supporting literature.
            :param substanceReference: None
            :param substanceCodeableConcept: None
            :param amountQuantity: None
            :param amountRange: None
            :param amountRatio: None
            :param amountString: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            relationship=relationship,
            isDefining=isDefining,
            amountRatioLowLimit=amountRatioLowLimit,
            amountType=amountType,
            source=source,
            substanceReference=substanceReference,
            substanceCodeableConcept=substanceCodeableConcept,
            amountQuantity=amountQuantity,
            amountRange=amountRange,
            amountRatio=amountRatio,
            amountString=amountString,
        )
