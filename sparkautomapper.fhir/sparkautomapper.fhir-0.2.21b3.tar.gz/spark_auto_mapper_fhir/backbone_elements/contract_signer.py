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
    # type_ (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.contract_signer_type_codes import (
        ContractSignerTypeCodesCode,
    )

    # End Import for CodeableConcept for type_
    # party (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for party
    from spark_auto_mapper_fhir.resources.organization import Organization
    from spark_auto_mapper_fhir.resources.patient import Patient
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

    # signature (Signature)
    from spark_auto_mapper_fhir.complex_types.signature import Signature


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ContractSigner(FhirBackboneElementBase):
    """
    Contract.Signer
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type_: Coding[ContractSignerTypeCodesCode],
        party: Reference[
            Union[Organization, Patient, Practitioner, PractitionerRole, RelatedPerson]
        ],
        signature: FhirList[Signature],
    ) -> None:
        """

        :param id_: id of resource
        :param extension: extensions
        :param type_: Role of this Contract signer, e.g. notary, grantee.
        :param party: Party which is a signator to this Contract.
        :param signature: Legally binding Contract DSIG signature contents in Base64.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            party=party,
            signature=signature,
        )
