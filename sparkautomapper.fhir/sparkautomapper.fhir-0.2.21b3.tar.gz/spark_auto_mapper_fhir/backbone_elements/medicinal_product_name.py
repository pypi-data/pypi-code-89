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
    # productName (string)
    # namePart (MedicinalProduct.NamePart)
    from spark_auto_mapper_fhir.backbone_elements.medicinal_product_name_part import (
        MedicinalProductNamePart,
    )

    # countryLanguage (MedicinalProduct.CountryLanguage)
    from spark_auto_mapper_fhir.backbone_elements.medicinal_product_country_language import (
        MedicinalProductCountryLanguage,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicinalProductName(FhirBackboneElementBase):
    """
    MedicinalProduct.Name
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        productName: FhirString,
        namePart: Optional[FhirList[MedicinalProductNamePart]] = None,
        countryLanguage: Optional[FhirList[MedicinalProductCountryLanguage]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param productName: The full product name.
        :param namePart: Coding words or phrases of the name.
        :param countryLanguage: Country where the name applies.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            productName=productName,
            namePart=namePart,
            countryLanguage=countryLanguage,
        )
