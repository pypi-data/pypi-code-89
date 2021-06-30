from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # collector (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for collector
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # duration (Duration)
    from spark_auto_mapper_fhir.complex_types.duration import Duration

    # quantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # method (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for method
    # Import for CodeableConcept for method
    from spark_auto_mapper_fhir.value_sets.fhir_specimen_collection_method import (
        FHIRSpecimenCollectionMethodCode,
    )

    # End Import for CodeableConcept for method
    # bodySite (CodeableConcept)
    # End Import for References for bodySite
    # Import for CodeableConcept for bodySite
    from spark_auto_mapper_fhir.value_sets.snomedct_body_structures import (
        SNOMEDCTBodyStructuresCode,
    )

    # End Import for CodeableConcept for bodySite
    # collectedDateTime (dateTime)
    # collectedPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # fastingStatusCodeableConcept (CodeableConcept)
    # End Import for References for fastingStatusCodeableConcept
    # Import for CodeableConcept for fastingStatusCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for fastingStatusCodeableConcept
    # fastingStatusDuration (Duration)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SpecimenCollection(FhirBackboneElementBase):
    """
    Specimen.Collection
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        collector: Optional[Reference[Union[Practitioner, PractitionerRole]]] = None,
        duration: Optional[Duration] = None,
        quantity: Optional[Quantity] = None,
        method: Optional[CodeableConcept[FHIRSpecimenCollectionMethodCode]] = None,
        bodySite: Optional[CodeableConcept[SNOMEDCTBodyStructuresCode]] = None,
        collectedDateTime: Optional[FhirDateTime] = None,
        collectedPeriod: Optional[Period] = None,
        fastingStatusCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        fastingStatusDuration: Optional[Duration] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param collector: Person who collected the specimen.
            :param duration: The span of time over which the collection of a specimen occurred.
            :param quantity: The quantity of specimen collected; for instance the volume of a blood sample,
        or the physical measurement of an anatomic pathology sample.
            :param method: A coded value specifying the technique that is used to perform the procedure.
            :param bodySite: Anatomical location from which the specimen was collected (if subject is a
        patient). This is the target site.  This element is not used for environmental
        specimens.
            :param collectedDateTime: None
            :param collectedPeriod: None
            :param fastingStatusCodeableConcept: None
            :param fastingStatusDuration: None
        """
        super().__init__(
            id_=id_,
            extension=extension,
            collector=collector,
            duration=duration,
            quantity=quantity,
            method=method,
            bodySite=bodySite,
            collectedDateTime=collectedDateTime,
            collectedPeriod=collectedPeriod,
            fastingStatusCodeableConcept=fastingStatusCodeableConcept,
            fastingStatusDuration=fastingStatusDuration,
        )
