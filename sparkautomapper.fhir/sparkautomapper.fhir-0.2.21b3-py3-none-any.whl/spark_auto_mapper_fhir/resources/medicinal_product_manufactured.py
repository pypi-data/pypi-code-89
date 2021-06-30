from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.medicinalproductmanufactured import (
    MedicinalProductManufacturedSchema,
)

if TYPE_CHECKING:
    pass
    # manufacturedDoseForm (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for manufacturedDoseForm
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for manufacturedDoseForm
    # unitOfPresentation (CodeableConcept)
    # Import for CodeableConcept for unitOfPresentation
    # End Import for CodeableConcept for unitOfPresentation
    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # manufacturer (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for manufacturer
    from spark_auto_mapper_fhir.resources.organization import Organization

    # ingredient (Reference)
    # Imports for References for ingredient
    from spark_auto_mapper_fhir.resources.medicinal_product_ingredient import (
        MedicinalProductIngredient,
    )

    # physicalCharacteristics (ProdCharacteristic)
    from spark_auto_mapper_fhir.backbone_elements.prod_characteristic import (
        ProdCharacteristic,
    )

    # otherCharacteristics (CodeableConcept)
    # Import for CodeableConcept for otherCharacteristics
    # End Import for CodeableConcept for otherCharacteristics


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicinalProductManufactured(FhirResourceBase):
    """
    MedicinalProductManufactured
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        manufacturedDoseForm: CodeableConcept[GenericTypeCode],
        unitOfPresentation: Optional[CodeableConcept[GenericTypeCode]] = None,
        quantity: Quantity,
        manufacturer: Optional[FhirList[Reference[Union[Organization]]]] = None,
        ingredient: Optional[
            FhirList[Reference[Union[MedicinalProductIngredient]]]
        ] = None,
        physicalCharacteristics: Optional[ProdCharacteristic] = None,
        otherCharacteristics: Optional[
            FhirList[CodeableConcept[GenericTypeCode]]
        ] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param manufacturedDoseForm: Dose form as manufactured and before any transformation into the
        pharmaceutical product.
            :param unitOfPresentation: The “real world” units in which the quantity of the manufactured item is
        described.
            :param quantity: The quantity or "count number" of the manufactured item.
            :param manufacturer: Manufacturer of the item (Note that this should be named "manufacturer" but it
        currently causes technical issues).
            :param ingredient: Ingredient.
            :param physicalCharacteristics: Dimensions, color etc.
            :param otherCharacteristics: Other codeable characteristics.
        """
        super().__init__(
            resourceType="MedicinalProductManufactured",
            id_=id_,
            meta=meta,
            extension=extension,
            manufacturedDoseForm=manufacturedDoseForm,
            unitOfPresentation=unitOfPresentation,
            quantity=quantity,
            manufacturer=manufacturer,
            ingredient=ingredient,
            physicalCharacteristics=physicalCharacteristics,
            otherCharacteristics=otherCharacteristics,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MedicinalProductManufacturedSchema.get_schema(
            include_extension=include_extension
        )
