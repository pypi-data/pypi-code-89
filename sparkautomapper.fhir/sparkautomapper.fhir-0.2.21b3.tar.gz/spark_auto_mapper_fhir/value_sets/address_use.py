from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AddressUseCode(FhirValueSetBase):
    """
    AddressUse
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/address-use
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/address-use"


class AddressUseCodeValues:
    """
    A communication address at a home.
    """

    Home = AddressUseCode("home")
    """
    An office address. First choice for business related contacts during business hours.
    """
    Work = AddressUseCode("work")
    """
    A temporary address. The period can provide more detailed information.
    """
    Temporary = AddressUseCode("temp")
    """
    This address is no longer in use (or was never correct but retained for records).
    """
    Old_Incorrect = AddressUseCode("old")
    """
    An address to be used to send bills, invoices, receipts etc.
    """
    Billing = AddressUseCode("billing")
