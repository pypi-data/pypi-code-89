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
    # reference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for reference
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.device import Device
    from spark_auto_mapper_fhir.resources.group import Group
    from spark_auto_mapper_fhir.resources.organization import Organization

    # role (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for role
    # Import for CodeableConcept for role
    from spark_auto_mapper_fhir.value_sets.contract_actor_role_codes import (
        ContractActorRoleCodesCode,
    )

    # End Import for CodeableConcept for role


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractSubject(FhirBackboneElementBase):
    """
    Contract.Subject
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        reference: FhirList[
            Reference[
                Union[
                    Patient,
                    RelatedPerson,
                    Practitioner,
                    PractitionerRole,
                    Device,
                    Group,
                    Organization,
                ]
            ]
        ],
        role: Optional[CodeableConcept[ContractActorRoleCodesCode]] = None,
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param reference: The entity the action is performed or not performed on or for.
        :param role: Role type of agent assigned roles in this Contract.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            reference=reference,
            role=role,
        )
