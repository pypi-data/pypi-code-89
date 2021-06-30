from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Can_push_updatesCode(FhirValueSetBase):
    """
    can-push-updates
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/verificationresult-can-push-updates
    """
    codeset: FhirUri = (
        "http://hl7.org/fhir/ValueSet/verificationresult-can-push-updates"
    )


class Can_push_updatesCodeValues:
    """
    None
    """

    Yes = Can_push_updatesCode("yes")
    """
    None
    """
    No = Can_push_updatesCode("no")
    """
    None
    """
    Undetermined = Can_push_updatesCode("undetermined")
