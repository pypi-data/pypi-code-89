from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.auditevent import AuditEventSchema

if TYPE_CHECKING:
    pass
    # type_ (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.audit_event_id import AuditEventIDCode

    # End Import for CodeableConcept for type_
    # subtype (Coding)
    # Import for CodeableConcept for subtype
    from spark_auto_mapper_fhir.value_sets.audit_event_sub__type import (
        AuditEventSub_TypeCode,
    )

    # End Import for CodeableConcept for subtype
    # action (AuditEventAction)
    from spark_auto_mapper_fhir.value_sets.audit_event_action import (
        AuditEventActionCode,
    )

    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # recorded (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # outcome (AuditEventOutcome)
    from spark_auto_mapper_fhir.value_sets.audit_event_outcome import (
        AuditEventOutcomeCode,
    )

    # outcomeDesc (string)
    # purposeOfEvent (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for purposeOfEvent
    from spark_auto_mapper_fhir.value_sets.purpose_of_use import PurposeOfUse

    # End Import for CodeableConcept for purposeOfEvent
    # agent (AuditEvent.Agent)
    from spark_auto_mapper_fhir.backbone_elements.audit_event_agent import (
        AuditEventAgent,
    )

    # source (AuditEvent.Source)
    from spark_auto_mapper_fhir.backbone_elements.audit_event_source import (
        AuditEventSource,
    )

    # entity (AuditEvent.Entity)
    from spark_auto_mapper_fhir.backbone_elements.audit_event_entity import (
        AuditEventEntity,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class AuditEvent(FhirResourceBase):
    """
    AuditEvent
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type_: Coding[AuditEventIDCode],
        subtype: Optional[FhirList[Coding[AuditEventSub_TypeCode]]] = None,
        action: Optional[AuditEventActionCode] = None,
        period: Optional[Period] = None,
        recorded: FhirInstant,
        outcome: Optional[AuditEventOutcomeCode] = None,
        outcomeDesc: Optional[FhirString] = None,
        purposeOfEvent: Optional[FhirList[CodeableConcept[PurposeOfUse]]] = None,
        agent: FhirList[AuditEventAgent],
        source: AuditEventSource,
        entity: Optional[FhirList[AuditEventEntity]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param type_: Identifier for a family of the event.  For example, a menu item, program,
        rule, policy, function code, application name or URL. It identifies the
        performed function.
            :param subtype: Identifier for the category of event.
            :param action: Indicator for type of action performed during the event that generated the
        audit.
            :param period: The period during which the activity occurred.
            :param recorded: The time when the event was recorded.
            :param outcome: Indicates whether the event succeeded or failed.
            :param outcomeDesc: A free text description of the outcome of the event.
            :param purposeOfEvent: The purposeOfUse (reason) that was used during the event being recorded.
            :param agent: An actor taking an active role in the event or activity that is logged.
            :param source: The system that is reporting the event.
            :param entity: Specific instances of data or objects that have been accessed.
        """
        super().__init__(
            resourceType="AuditEvent",
            id_=id_,
            meta=meta,
            extension=extension,
            type_=type_,
            subtype=subtype,
            action=action,
            period=period,
            recorded=recorded,
            outcome=outcome,
            outcomeDesc=outcomeDesc,
            purposeOfEvent=purposeOfEvent,
            agent=agent,
            source=source,
            entity=entity,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return AuditEventSchema.get_schema(include_extension=include_extension)
