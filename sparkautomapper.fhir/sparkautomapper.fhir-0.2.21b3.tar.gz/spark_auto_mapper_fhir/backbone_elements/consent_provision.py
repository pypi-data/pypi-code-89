from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # type_ (ConsentProvisionType)
    from spark_auto_mapper_fhir.value_sets.consent_provision_type import (
        ConsentProvisionTypeCode,
    )

    # period (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # actor (Consent.Actor)
    from spark_auto_mapper_fhir.backbone_elements.consent_actor import ConsentActor

    # action (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for action
    # Import for CodeableConcept for action
    from spark_auto_mapper_fhir.value_sets.consent_action_codes import (
        ConsentActionCodesCode,
    )

    # End Import for CodeableConcept for action
    # securityLabel (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # End Import for References for securityLabel
    # Import for CodeableConcept for securityLabel
    from spark_auto_mapper_fhir.value_sets.all_security_labels import (
        AllSecurityLabelsCode,
    )

    # End Import for CodeableConcept for securityLabel
    # purpose (Coding)
    # End Import for References for purpose
    # Import for CodeableConcept for purpose
    from spark_auto_mapper_fhir.value_sets.purpose_of_use import PurposeOfUse

    # End Import for CodeableConcept for purpose
    # class_ (Coding)
    # End Import for References for class_
    # Import for CodeableConcept for class_
    from spark_auto_mapper_fhir.value_sets.consent_content_class import (
        ConsentContentClassCode,
    )

    # End Import for CodeableConcept for class_
    # code (CodeableConcept)
    # End Import for References for code
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.consent_content_codes import (
        ConsentContentCodesCode,
    )

    # End Import for CodeableConcept for code
    # dataPeriod (Period)
    # data (Consent.Data)
    from spark_auto_mapper_fhir.backbone_elements.consent_data import ConsentData


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ConsentProvision(FhirBackboneElementBase):
    """
    Consent.Provision
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type_: Optional[ConsentProvisionTypeCode] = None,
        period: Optional[Period] = None,
        actor: Optional[FhirList[ConsentActor]] = None,
        action: Optional[FhirList[CodeableConcept[ConsentActionCodesCode]]] = None,
        securityLabel: Optional[FhirList[Coding[AllSecurityLabelsCode]]] = None,
        purpose: Optional[FhirList[Coding[PurposeOfUse]]] = None,
        class_: Optional[FhirList[Coding[ConsentContentClassCode]]] = None,
        code: Optional[FhirList[CodeableConcept[ConsentContentCodesCode]]] = None,
        dataPeriod: Optional[Period] = None,
        data: Optional[FhirList[ConsentData]] = None,
        provision: Optional[FhirList[ConsentProvision]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param type_: Action  to take - permit or deny - when the rule conditions are met.  Not
        permitted in root rule, required in all nested rules.
            :param period: The timeframe in this rule is valid.
            :param actor: Who or what is controlled by this rule. Use group to identify a set of actors
        by some property they share (e.g. 'admitting officers').
            :param action: Actions controlled by this Rule.
            :param securityLabel: A security label, comprised of 0..* security label fields (Privacy tags),
        which define which resources are controlled by this exception.
            :param purpose: The context of the activities a user is taking - why the user is accessing the
        data - that are controlled by this rule.
            :param class_: The class of information covered by this rule. The type can be a FHIR resource
        type, a profile on a type, or a CDA document, or some other type that
        indicates what sort of information the consent relates to.
            :param code: If this code is found in an instance, then the rule applies.
            :param dataPeriod: Clinical or Operational Relevant period of time that bounds the data
        controlled by this rule.
            :param data: The resources controlled by this rule if specific resources are referenced.
            :param provision: Rules which provide exceptions to the base rule or subrules.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            period=period,
            actor=actor,
            action=action,
            securityLabel=securityLabel,
            purpose=purpose,
            class_=class_,
            code=code,
            dataPeriod=dataPeriod,
            data=data,
            provision=provision,
        )
