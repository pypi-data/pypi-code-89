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
    # role (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for role
    # Import for CodeableConcept for role
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for role
    # actor (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for actor
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class InvoiceParticipant(FhirBackboneElementBase):
    """
    Invoice.Participant
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        role: Optional[CodeableConcept[GenericTypeCode]] = None,
        actor: Reference[
            Union[
                Practitioner,
                Organization,
                Patient,
                PractitionerRole,
                Device,
                RelatedPerson,
            ]
        ],
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param role: Describes the type of involvement (e.g. transcriptionist, creator etc.). If
        the invoice has been created automatically, the Participant may be a billing
        engine or another kind of device.
            :param actor: The device, practitioner, etc. who performed or participated in the service.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            role=role,
            actor=actor,
        )
