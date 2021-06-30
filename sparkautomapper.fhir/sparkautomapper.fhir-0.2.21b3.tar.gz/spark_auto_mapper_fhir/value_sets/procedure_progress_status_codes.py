from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ProcedureProgressStatusCodesCode(FhirValueSetBase):
    """
    ProcedureProgressStatusCodes
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/procedure-progress-status-codes
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/procedure-progress-status-codes"


class ProcedureProgressStatusCodesCodeValues:
    """
    A patient is in the Operating Room.
    """

    InOperatingRoom = ProcedureProgressStatusCodesCode("in-operating-room")
    """
    The patient is prepared for a procedure.
    """
    Prepared = ProcedureProgressStatusCodesCode("prepared")
    """
    The patient is under anesthesia.
    """
    AnesthesiaInduced = ProcedureProgressStatusCodesCode("anesthesia-induced")
    """
    The patient has open incision(s).
    """
    OpenIncision = ProcedureProgressStatusCodesCode("open-incision")
    """
    The patient has incision(s) closed.
    """
    ClosedIncision = ProcedureProgressStatusCodesCode("closed-incision")
    """
    The patient is in the recovery room.
    """
    InRecoveryRoom = ProcedureProgressStatusCodesCode("in-recovery-room")
