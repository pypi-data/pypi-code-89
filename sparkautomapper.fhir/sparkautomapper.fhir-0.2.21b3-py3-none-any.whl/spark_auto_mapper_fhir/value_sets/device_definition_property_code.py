from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DeviceDefinitionPropertyCodeCode(FhirValueSetBase):
    """
    DeviceDefinitionPropertyCode
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/ValueSet/device-component-property
    """
    codeset: FhirUri = "http://hl7.org/fhir/ValueSet/device-component-property"


class DeviceDefinitionPropertyCodeCodeValues:
    """
    None
    """

    MDC_TIME_CAP_STATE = DeviceDefinitionPropertyCodeCode("68219")
    """
    None
    """
    MDC_TIME_SYNC_PROTOCOL = DeviceDefinitionPropertyCodeCode("68220")
    """
    None
    """
    MDC_TIME_SYNC_ACCURACY = DeviceDefinitionPropertyCodeCode("68221")
    """
    None
    """
    MDC_TIME_RES_ABS = DeviceDefinitionPropertyCodeCode("68222")
    """
    None
    """
    MDC_TIME_RES_REL = DeviceDefinitionPropertyCodeCode("68223")
    """
    None
    """
    MDC_TIME_RES_REL_HI_RES = DeviceDefinitionPropertyCodeCode("68224")
    """
    None
    """
    MDC_TIME_RES_BO = DeviceDefinitionPropertyCodeCode("68226")
    """
    None
    """
    MDC_REG_CERT_DATA_CONTINUA_CERT_DEV_LIST = DeviceDefinitionPropertyCodeCode(
        "532353"
    )
    """
    None
    """
    MDC_REG_CERT_DATA_CONTINUA_REG_STATUS = DeviceDefinitionPropertyCodeCode("532354")
    """
    None
    """
    MDC_REG_CERT_DATA_CONTINUA_PHG_CERT_LIST = DeviceDefinitionPropertyCodeCode(
        "532355"
    )
