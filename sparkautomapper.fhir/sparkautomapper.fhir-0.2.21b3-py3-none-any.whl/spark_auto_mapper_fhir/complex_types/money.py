from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase

if TYPE_CHECKING:
    pass
    # value (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

    # currency (Currencies)
    from spark_auto_mapper_fhir.value_sets.currencies import CurrenciesCode


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Money(FhirComplexTypeBase):
    """
    Money
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        value: Optional[FhirDecimal] = None,
        currency: Optional[CurrenciesCode] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param value: Numerical value (with implicit precision).
        :param currency: ISO 4217 Currency Code.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            value=value,
            currency=currency,
        )
