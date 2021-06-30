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
    # sequence (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # priceComponent (Invoice.PriceComponent)
    from spark_auto_mapper_fhir.backbone_elements.invoice_price_component import (
        InvoicePriceComponent,
    )

    # chargeItemReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for chargeItemReference
    from spark_auto_mapper_fhir.resources.charge_item import ChargeItem

    # chargeItemCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for chargeItemCodeableConcept
    # Import for CodeableConcept for chargeItemCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for chargeItemCodeableConcept


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class InvoiceLineItem(FhirBackboneElementBase):
    """
    Invoice.LineItem
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        sequence: Optional[FhirPositiveInt] = None,
        priceComponent: Optional[FhirList[InvoicePriceComponent]] = None,
        chargeItemReference: Optional[Reference[Union[ChargeItem]]] = None,
        chargeItemCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param sequence: Sequence in which the items appear on the invoice.
            :param priceComponent: The price for a ChargeItem may be calculated as a base price with
        surcharges/deductions that apply in certain conditions. A ChargeItemDefinition
        resource that defines the prices, factors and conditions that apply to a
        billing code is currently under development. The priceComponent element can be
        used to offer transparency to the recipient of the Invoice as to how the
        prices have been calculated.
            :param chargeItemReference: None
            :param chargeItemCodeableConcept: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            sequence=sequence,
            priceComponent=priceComponent,
            chargeItemReference=chargeItemReference,
            chargeItemCodeableConcept=chargeItemCodeableConcept,
        )
