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
    # location (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for location
    from spark_auto_mapper_fhir.resources.location import Location

    # status (EncounterLocationStatus)
    from spark_auto_mapper_fhir.value_sets.encounter_location_status import (
        EncounterLocationStatusCode,
    )

    # physicalType (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for physicalType
    # Import for CodeableConcept for physicalType
    from spark_auto_mapper_fhir.value_sets.location_type import LocationTypeCode

    # End Import for CodeableConcept for physicalType
    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EncounterLocation(FhirBackboneElementBase):
    """
    Encounter.Location
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        location: Reference[Union[Location]],
        status: Optional[EncounterLocationStatusCode] = None,
        physicalType: Optional[CodeableConcept[LocationTypeCode]] = None,
        period: Optional[Period] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param location: The location where the encounter takes place.
            :param status: The status of the participants' presence at the specified location during the
        period specified. If the participant is no longer at the location, then the
        period will have an end date/time.
            :param physicalType: This will be used to specify the required levels (bed/ward/room/etc.) desired
        to be recorded to simplify either messaging or query.
            :param period: Time period during which the patient was present at the location.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            location=location,
            status=status,
            physicalType=physicalType,
            period=period,
        )
