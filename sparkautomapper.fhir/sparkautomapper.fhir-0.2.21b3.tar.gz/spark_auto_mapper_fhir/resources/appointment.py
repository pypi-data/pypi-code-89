from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.appointment import AppointmentSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # status (AppointmentStatus)
    from spark_auto_mapper_fhir.value_sets.appointment_status import (
        AppointmentStatusCode,
    )

    # cancelationReason (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for cancelationReason
    from spark_auto_mapper_fhir.value_sets.appointment_cancellation_reason import (
        AppointmentCancellationReasonCode,
    )

    # End Import for CodeableConcept for cancelationReason
    # serviceCategory (CodeableConcept)
    # Import for CodeableConcept for serviceCategory
    from spark_auto_mapper_fhir.value_sets.service_category import ServiceCategoryCode

    # End Import for CodeableConcept for serviceCategory
    # serviceType (CodeableConcept)
    # Import for CodeableConcept for serviceType
    from spark_auto_mapper_fhir.value_sets.service_type import ServiceTypeCode

    # End Import for CodeableConcept for serviceType
    # specialty (CodeableConcept)
    # Import for CodeableConcept for specialty
    from spark_auto_mapper_fhir.value_sets.practice_setting_code_value_set import (
        PracticeSettingCodeValueSetCode,
    )

    # End Import for CodeableConcept for specialty
    # appointmentType (CodeableConcept)
    # Import for CodeableConcept for appointmentType
    from spark_auto_mapper_fhir.value_sets.v2_0276 import V2_0276

    # End Import for CodeableConcept for appointmentType
    # reasonCode (CodeableConcept)
    # Import for CodeableConcept for reasonCode
    from spark_auto_mapper_fhir.value_sets.encounter_reason_codes import (
        EncounterReasonCodesCode,
    )

    # End Import for CodeableConcept for reasonCode
    # reasonReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for reasonReference
    from spark_auto_mapper_fhir.resources.condition import Condition
    from spark_auto_mapper_fhir.resources.procedure import Procedure
    from spark_auto_mapper_fhir.resources.observation import Observation
    from spark_auto_mapper_fhir.resources.immunization_recommendation import (
        ImmunizationRecommendation,
    )

    # priority (unsignedInt)
    from spark_auto_mapper_fhir.complex_types.unsigned_int import unsignedInt

    # description (string)
    # supportingInformation (Reference)
    # Imports for References for supportingInformation
    from spark_auto_mapper_fhir.resources.resource import Resource

    # start (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # end (instant)
    # minutesDuration (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # slot (Reference)
    # Imports for References for slot
    from spark_auto_mapper_fhir.resources.slot import Slot

    # created (dateTime)
    # comment (string)
    # patientInstruction (string)
    # basedOn (Reference)
    # Imports for References for basedOn
    from spark_auto_mapper_fhir.resources.service_request import ServiceRequest

    # participant (Appointment.Participant)
    from spark_auto_mapper_fhir.backbone_elements.appointment_participant import (
        AppointmentParticipant,
    )

    # requestedPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Appointment(FhirResourceBase):
    """
    Appointment
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: AppointmentStatusCode,
        cancelationReason: Optional[
            CodeableConcept[AppointmentCancellationReasonCode]
        ] = None,
        serviceCategory: Optional[
            FhirList[CodeableConcept[ServiceCategoryCode]]
        ] = None,
        serviceType: Optional[FhirList[CodeableConcept[ServiceTypeCode]]] = None,
        specialty: Optional[
            FhirList[CodeableConcept[PracticeSettingCodeValueSetCode]]
        ] = None,
        appointmentType: Optional[CodeableConcept[V2_0276]] = None,
        reasonCode: Optional[
            FhirList[CodeableConcept[EncounterReasonCodesCode]]
        ] = None,
        reasonReference: Optional[
            FhirList[
                Reference[
                    Union[Condition, Procedure, Observation, ImmunizationRecommendation]
                ]
            ]
        ] = None,
        priority: Optional[unsignedInt] = None,
        description: Optional[FhirString] = None,
        supportingInformation: Optional[FhirList[Reference[Union[Resource]]]] = None,
        start: Optional[FhirInstant] = None,
        end: Optional[FhirInstant] = None,
        minutesDuration: Optional[FhirPositiveInt] = None,
        slot: Optional[FhirList[Reference[Union[Slot]]]] = None,
        created: Optional[FhirDateTime] = None,
        comment: Optional[FhirString] = None,
        patientInstruction: Optional[FhirString] = None,
        basedOn: Optional[FhirList[Reference[Union[ServiceRequest]]]] = None,
        participant: FhirList[AppointmentParticipant],
        requestedPeriod: Optional[FhirList[Period]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: This records identifiers associated with this appointment concern that are
        defined by business processes and/or used to refer to it when a direct URL
        reference to the resource itself is not appropriate (e.g. in CDA documents, or
        in written / printed documentation).
            :param status: The overall status of the Appointment. Each of the participants has their own
        participation status which indicates their involvement in the process, however
        this status indicates the shared status.
            :param cancelationReason: The coded reason for the appointment being cancelled. This is often used in
        reporting/billing/futher processing to determine if further actions are
        required, or specific fees apply.
            :param serviceCategory: A broad categorization of the service that is to be performed during this
        appointment.
            :param serviceType: The specific service that is to be performed during this appointment.
            :param specialty: The specialty of a practitioner that would be required to perform the service
        requested in this appointment.
            :param appointmentType: The style of appointment or patient that has been booked in the slot (not
        service type).
            :param reasonCode: The coded reason that this appointment is being scheduled. This is more
        clinical than administrative.
            :param reasonReference: Reason the appointment has been scheduled to take place, as specified using
        information from another resource. When the patient arrives and the encounter
        begins it may be used as the admission diagnosis. The indication will
        typically be a Condition (with other resources referenced in the
        evidence.detail), or a Procedure.
            :param priority: The priority of the appointment. Can be used to make informed decisions if
        needing to re-prioritize appointments. (The iCal Standard specifies 0 as
        undefined, 1 as highest, 9 as lowest priority).
            :param description: The brief description of the appointment as would be shown on a subject line
        in a meeting request, or appointment list. Detailed or expanded information
        should be put in the comment field.
            :param supportingInformation: Additional information to support the appointment provided when making the
        appointment.
            :param start: Date/Time that the appointment is to take place.
            :param end: Date/Time that the appointment is to conclude.
            :param minutesDuration: Number of minutes that the appointment is to take. This can be less than the
        duration between the start and end times.  For example, where the actual time
        of appointment is only an estimate or if a 30 minute appointment is being
        requested, but any time would work.  Also, if there is, for example, a planned
        15 minute break in the middle of a long appointment, the duration may be 15
        minutes less than the difference between the start and end.
            :param slot: The slots from the participants' schedules that will be filled by the
        appointment.
            :param created: The date that this appointment was initially created. This could be different
        to the meta.lastModified value on the initial entry, as this could have been
        before the resource was created on the FHIR server, and should remain
        unchanged over the lifespan of the appointment.
            :param comment: Additional comments about the appointment.
            :param patientInstruction: While Appointment.comment contains information for internal use,
        Appointment.patientInstructions is used to capture patient facing information
        about the Appointment (e.g. please bring your referral or fast from 8pm night
        before).
            :param basedOn: The service request this appointment is allocated to assess (e.g. incoming
        referral or procedure request).
            :param participant: List of participants involved in the appointment.
            :param requestedPeriod: A set of date ranges (potentially including times) that the appointment is
        preferred to be scheduled within.

        The duration (usually in minutes) could also be provided to indicate the
        length of the appointment to fill and populate the start/end times for the
        actual allocated time. However, in other situations the duration may be
        calculated by the scheduling system.
        """
        super().__init__(
            resourceType="Appointment",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            cancelationReason=cancelationReason,
            serviceCategory=serviceCategory,
            serviceType=serviceType,
            specialty=specialty,
            appointmentType=appointmentType,
            reasonCode=reasonCode,
            reasonReference=reasonReference,
            priority=priority,
            description=description,
            supportingInformation=supportingInformation,
            start=start,
            end=end,
            minutesDuration=minutesDuration,
            slot=slot,
            created=created,
            comment=comment,
            patientInstruction=patientInstruction,
            basedOn=basedOn,
            participant=participant,
            requestedPeriod=requestedPeriod,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return AppointmentSchema.get_schema(include_extension=include_extension)
