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
    # name (string)
    # type_ (DeviceNameType)
    from spark_auto_mapper_fhir.value_sets.device_name_type import DeviceNameTypeCode


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DeviceDeviceName(FhirBackboneElementBase):
    """
    Device.DeviceName
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        name: FhirString,
        type_: DeviceNameTypeCode,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param name: The name of the device.
            :param type_: The type of deviceName.
        UDILabelName | UserFriendlyName | PatientReportedName | ManufactureDeviceName
        | ModelName.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            name=name,
            type_=type_,
        )
