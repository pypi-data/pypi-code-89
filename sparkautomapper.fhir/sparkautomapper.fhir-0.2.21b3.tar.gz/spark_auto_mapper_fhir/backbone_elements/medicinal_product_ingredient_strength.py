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
    # presentation (Ratio)
    from spark_auto_mapper_fhir.complex_types.ratio import Ratio

    # presentationLowLimit (Ratio)
    # concentration (Ratio)
    # concentrationLowLimit (Ratio)
    # measurementPoint (string)
    # country (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for country
    # Import for CodeableConcept for country
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for country
    # referenceStrength (MedicinalProductIngredient.ReferenceStrength)
    from spark_auto_mapper_fhir.backbone_elements.medicinal_product_ingredient_reference_strength import (
        MedicinalProductIngredientReferenceStrength,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicinalProductIngredientStrength(FhirBackboneElementBase):
    """
    MedicinalProductIngredient.Strength
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        presentation: Ratio,
        presentationLowLimit: Optional[Ratio] = None,
        concentration: Optional[Ratio] = None,
        concentrationLowLimit: Optional[Ratio] = None,
        measurementPoint: Optional[FhirString] = None,
        country: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        referenceStrength: Optional[
            FhirList[MedicinalProductIngredientReferenceStrength]
        ] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param presentation: The quantity of substance in the unit of presentation, or in the volume (or
        mass) of the single pharmaceutical product or manufactured item.
            :param presentationLowLimit: A lower limit for the quantity of substance in the unit of presentation. For
        use when there is a range of strengths, this is the lower limit, with the
        presentation attribute becoming the upper limit.
            :param concentration: The strength per unitary volume (or mass).
            :param concentrationLowLimit: A lower limit for the strength per unitary volume (or mass), for when there is
        a range. The concentration attribute then becomes the upper limit.
            :param measurementPoint: For when strength is measured at a particular point or distance.
            :param country: The country or countries for which the strength range applies.
            :param referenceStrength: Strength expressed in terms of a reference substance.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            presentation=presentation,
            presentationLowLimit=presentationLowLimit,
            concentration=concentration,
            concentrationLowLimit=concentrationLowLimit,
            measurementPoint=measurementPoint,
            country=country,
            referenceStrength=referenceStrength,
        )
