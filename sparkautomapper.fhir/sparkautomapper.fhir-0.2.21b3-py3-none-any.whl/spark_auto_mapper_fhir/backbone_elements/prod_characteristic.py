from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # height (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # width (Quantity)
    # depth (Quantity)
    # weight (Quantity)
    # nominalVolume (Quantity)
    # externalDiameter (Quantity)
    # shape (string)
    # color (string)
    # imprint (string)
    # image (Attachment)
    from spark_auto_mapper_fhir.complex_types.attachment import Attachment

    # scoring (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for scoring
    # Import for CodeableConcept for scoring
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for scoring


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ProdCharacteristic(FhirBackboneElementBase):
    """
    ProdCharacteristic
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        height: Optional[Quantity] = None,
        width: Optional[Quantity] = None,
        depth: Optional[Quantity] = None,
        weight: Optional[Quantity] = None,
        nominalVolume: Optional[Quantity] = None,
        externalDiameter: Optional[Quantity] = None,
        shape: Optional[FhirString] = None,
        color: Optional[FhirList[FhirString]] = None,
        imprint: Optional[FhirList[FhirString]] = None,
        image: Optional[FhirList[Attachment]] = None,
        scoring: Optional[CodeableConcept[GenericTypeCode]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param height: Where applicable, the height can be specified using a numerical value and its
        unit of measurement The unit of measurement shall be specified in accordance
        with ISO 11240 and the resulting terminology The symbol and the symbol
        identifier shall be used.
            :param width: Where applicable, the width can be specified using a numerical value and its
        unit of measurement The unit of measurement shall be specified in accordance
        with ISO 11240 and the resulting terminology The symbol and the symbol
        identifier shall be used.
            :param depth: Where applicable, the depth can be specified using a numerical value and its
        unit of measurement The unit of measurement shall be specified in accordance
        with ISO 11240 and the resulting terminology The symbol and the symbol
        identifier shall be used.
            :param weight: Where applicable, the weight can be specified using a numerical value and its
        unit of measurement The unit of measurement shall be specified in accordance
        with ISO 11240 and the resulting terminology The symbol and the symbol
        identifier shall be used.
            :param nominalVolume: Where applicable, the nominal volume can be specified using a numerical value
        and its unit of measurement The unit of measurement shall be specified in
        accordance with ISO 11240 and the resulting terminology The symbol and the
        symbol identifier shall be used.
            :param externalDiameter: Where applicable, the external diameter can be specified using a numerical
        value and its unit of measurement The unit of measurement shall be specified
        in accordance with ISO 11240 and the resulting terminology The symbol and the
        symbol identifier shall be used.
            :param shape: Where applicable, the shape can be specified An appropriate controlled
        vocabulary shall be used The term and the term identifier shall be used.
            :param color: Where applicable, the color can be specified An appropriate controlled
        vocabulary shall be used The term and the term identifier shall be used.
            :param imprint: Where applicable, the imprint can be specified as text.
            :param image: Where applicable, the image can be provided The format of the image attachment
        shall be specified by regional implementations.
            :param scoring: Where applicable, the scoring can be specified An appropriate controlled
        vocabulary shall be used The term and the term identifier shall be used.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            height=height,
            width=width,
            depth=depth,
            weight=weight,
            nominalVolume=nominalVolume,
            externalDiameter=externalDiameter,
            shape=shape,
            color=color,
            imprint=imprint,
            image=image,
            scoring=scoring,
        )
