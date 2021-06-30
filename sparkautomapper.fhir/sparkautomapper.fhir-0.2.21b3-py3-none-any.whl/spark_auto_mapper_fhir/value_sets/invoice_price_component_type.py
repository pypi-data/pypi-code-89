from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class InvoicePriceComponentTypeCode(FhirValueSetBase):
    """
    InvoicePriceComponentType
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/invoice-priceComponentType
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/invoice-priceComponentType"


class InvoicePriceComponentTypeCodeValues:
    """
    the amount is the base price used for calculating the total price before applying surcharges, discount or taxes.
    """

    BasePrice = InvoicePriceComponentTypeCode("base")
    """
    the amount is a surcharge applied on the base price.
    """
    Surcharge = InvoicePriceComponentTypeCode("surcharge")
    """
    the amount is a deduction applied on the base price.
    """
    Deduction = InvoicePriceComponentTypeCode("deduction")
    """
    the amount is a discount applied on the base price.
    """
    Discount = InvoicePriceComponentTypeCode("discount")
    """
    the amount is the tax component of the total price.
    """
    Tax = InvoicePriceComponentTypeCode("tax")
    """
    the amount is of informational character, it has not been applied in the calculation of the total price.
    """
    Informational = InvoicePriceComponentTypeCode("informational")
