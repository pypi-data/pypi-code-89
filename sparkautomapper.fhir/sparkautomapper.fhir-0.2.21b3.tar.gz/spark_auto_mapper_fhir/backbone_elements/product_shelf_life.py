from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for type_
    # period (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # specialPrecautionsForStorage (CodeableConcept)
    # End Import for References for specialPrecautionsForStorage
    # Import for CodeableConcept for specialPrecautionsForStorage
    # End Import for CodeableConcept for specialPrecautionsForStorage


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ProductShelfLife(FhirBackboneElementBase):
    """
    ProductShelfLife
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[Identifier] = None,
        type_: CodeableConcept[GenericTypeCode],
        period: Quantity,
        specialPrecautionsForStorage: Optional[
            FhirList[CodeableConcept[GenericTypeCode]]
        ] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param identifier: Unique identifier for the packaged Medicinal Product.
            :param type_: This describes the shelf life, taking into account various scenarios such as
        shelf life of the packaged Medicinal Product itself, shelf life after
        transformation where necessary and shelf life after the first opening of a
        bottle, etc. The shelf life type shall be specified using an appropriate
        controlled vocabulary The controlled term and the controlled term identifier
        shall be specified.
            :param period: The shelf life time period can be specified using a numerical value for the
        period of time and its unit of time measurement The unit of measurement shall
        be specified in accordance with ISO 11240 and the resulting terminology The
        symbol and the symbol identifier shall be used.
            :param specialPrecautionsForStorage: Special precautions for storage, if any, can be specified using an appropriate
        controlled vocabulary The controlled term and the controlled term identifier
        shall be specified.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            identifier=identifier,
            type_=type_,
            period=period,
            specialPrecautionsForStorage=specialPrecautionsForStorage,
        )
