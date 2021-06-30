from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

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
    # target (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for target
    from spark_auto_mapper_fhir.resources.device import Device

    # endpoint (url)
    from spark_auto_mapper_fhir.complex_types.url import url

    # receiver (Reference)
    # Imports for References for receiver
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MessageHeaderDestination(FhirBackboneElementBase):
    """
    MessageHeader.Destination
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        name: Optional[FhirString] = None,
        target: Optional[Reference[Union[Device]]] = None,
        endpoint: url,
        receiver: Optional[
            Reference[Union[Practitioner, PractitionerRole, Organization]]
        ] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param name: Human-readable name for the target system.
            :param target: Identifies the target end system in situations where the initial message
        transmission is to an intermediary system.
            :param endpoint: Indicates where the message should be routed to.
            :param receiver: Allows data conveyed by a message to be addressed to a particular person or
        department when routing to a specific application isn't sufficient.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            name=name,
            target=target,
            endpoint=endpoint,
            receiver=receiver,
        )
