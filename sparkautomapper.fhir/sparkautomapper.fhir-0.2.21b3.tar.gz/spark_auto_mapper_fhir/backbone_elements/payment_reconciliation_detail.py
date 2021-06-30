from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.resource import Resource

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # predecessor (Identifier)
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.payment_type_codes import (
        PaymentTypeCodesCode,
    )

    # End Import for CodeableConcept for type_
    # request (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for request
    # submitter (Reference)
    # Imports for References for submitter
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization

    # response (Reference)
    # Imports for References for response
    # date (date)
    # responsible (Reference)
    # Imports for References for responsible
    # payee (Reference)
    # Imports for References for payee
    # amount (Money)
    from spark_auto_mapper_fhir.complex_types.money import Money


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PaymentReconciliationDetail(FhirBackboneElementBase):
    """
    PaymentReconciliation.Detail
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[Identifier] = None,
        predecessor: Optional[Identifier] = None,
        type_: CodeableConcept[PaymentTypeCodesCode],
        request: Optional[Reference[Union[Resource]]] = None,
        submitter: Optional[
            Reference[Union[Practitioner, PractitionerRole, Organization]]
        ] = None,
        response: Optional[Reference[Union[Resource]]] = None,
        date: Optional[FhirDate] = None,
        responsible: Optional[Reference[Union[PractitionerRole]]] = None,
        payee: Optional[
            Reference[Union[Practitioner, PractitionerRole, Organization]]
        ] = None,
        amount: Optional[Money] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param identifier: Unique identifier for the current payment item for the referenced payable.
            :param predecessor: Unique identifier for the prior payment item for the referenced payable.
            :param type_: Code to indicate the nature of the payment.
            :param request: A resource, such as a Claim, the evaluation of which could lead to payment.
            :param submitter: The party which submitted the claim or financial transaction.
            :param response: A resource, such as a ClaimResponse, which contains a commitment to payment.
            :param date: The date from the response resource containing a commitment to pay.
            :param responsible: A reference to the individual who is responsible for inquiries regarding the
        response and its payment.
            :param payee: The party which is receiving the payment.
            :param amount: The monetary amount allocated from the total payment to the payable.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            identifier=identifier,
            predecessor=predecessor,
            type_=type_,
            request=request,
            submitter=submitter,
            response=response,
            date=date,
            responsible=responsible,
            payee=payee,
            amount=amount,
        )
