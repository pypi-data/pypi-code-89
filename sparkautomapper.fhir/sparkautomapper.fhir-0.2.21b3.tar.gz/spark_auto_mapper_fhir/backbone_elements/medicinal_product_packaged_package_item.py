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
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for type_
    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # material (CodeableConcept)
    # End Import for References for material
    # Import for CodeableConcept for material
    # End Import for CodeableConcept for material
    # alternateMaterial (CodeableConcept)
    # End Import for References for alternateMaterial
    # Import for CodeableConcept for alternateMaterial
    # End Import for CodeableConcept for alternateMaterial
    # device (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for device
    from spark_auto_mapper_fhir.resources.device_definition import DeviceDefinition

    # manufacturedItem (Reference)
    # Imports for References for manufacturedItem
    from spark_auto_mapper_fhir.resources.medicinal_product_manufactured import (
        MedicinalProductManufactured,
    )

    # physicalCharacteristics (ProdCharacteristic)
    from spark_auto_mapper_fhir.backbone_elements.prod_characteristic import (
        ProdCharacteristic,
    )

    # otherCharacteristics (CodeableConcept)
    # End Import for References for otherCharacteristics
    # Import for CodeableConcept for otherCharacteristics
    # End Import for CodeableConcept for otherCharacteristics
    # shelfLifeStorage (ProductShelfLife)
    from spark_auto_mapper_fhir.backbone_elements.product_shelf_life import (
        ProductShelfLife,
    )

    # manufacturer (Reference)
    # Imports for References for manufacturer
    from spark_auto_mapper_fhir.resources.organization import Organization


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicinalProductPackagedPackageItem(FhirBackboneElementBase):
    """
    MedicinalProductPackaged.PackageItem
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        type_: CodeableConcept[GenericTypeCode],
        quantity: Quantity,
        material: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        alternateMaterial: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        device: Optional[FhirList[Reference[Union[DeviceDefinition]]]] = None,
        manufacturedItem: Optional[
            FhirList[Reference[Union[MedicinalProductManufactured]]]
        ] = None,
        packageItem: Optional[FhirList[MedicinalProductPackagedPackageItem]] = None,
        physicalCharacteristics: Optional[ProdCharacteristic] = None,
        otherCharacteristics: Optional[
            FhirList[CodeableConcept[GenericTypeCode]]
        ] = None,
        shelfLifeStorage: Optional[FhirList[ProductShelfLife]] = None,
        manufacturer: Optional[FhirList[Reference[Union[Organization]]]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param identifier: Including possibly Data Carrier Identifier.
            :param type_: The physical type of the container of the medicine.
            :param quantity: The quantity of this package in the medicinal product, at the current level of
        packaging. The outermost is always 1.
            :param material: Material type of the package item.
            :param alternateMaterial: A possible alternate material for the packaging.
            :param device: A device accompanying a medicinal product.
            :param manufacturedItem: The manufactured item as contained in the packaged medicinal product.
            :param packageItem: Allows containers within containers.
            :param physicalCharacteristics: Dimensions, color etc.
            :param otherCharacteristics: Other codeable characteristics.
            :param shelfLifeStorage: Shelf Life and storage information.
            :param manufacturer: Manufacturer of this Package Item.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            identifier=identifier,
            type_=type_,
            quantity=quantity,
            material=material,
            alternateMaterial=alternateMaterial,
            device=device,
            manufacturedItem=manufacturedItem,
            packageItem=packageItem,
            physicalCharacteristics=physicalCharacteristics,
            otherCharacteristics=otherCharacteristics,
            shelfLifeStorage=shelfLifeStorage,
            manufacturer=manufacturer,
        )
