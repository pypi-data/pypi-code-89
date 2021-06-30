from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.paymentnotice import PaymentNoticeSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # status (FinancialResourceStatusCodes)
    from spark_auto_mapper_fhir.value_sets.financial_resource_status_codes import (
        FinancialResourceStatusCodesCode,
    )

    # request (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for request
    from spark_auto_mapper_fhir.resources.resource import Resource

    # response (Reference)
    # Imports for References for response
    # created (dateTime)
    # provider (Reference)
    # Imports for References for provider
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
    from spark_auto_mapper_fhir.resources.organization import Organization

    # payment (Reference)
    # Imports for References for payment
    from spark_auto_mapper_fhir.resources.payment_reconciliation import (
        PaymentReconciliation,
    )

    # paymentDate (date)
    # payee (Reference)
    # Imports for References for payee
    # recipient (Reference)
    # Imports for References for recipient
    # amount (Money)
    from spark_auto_mapper_fhir.complex_types.money import Money

    # paymentStatus (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for paymentStatus
    from spark_auto_mapper_fhir.value_sets.payment_status_codes import (
        PaymentStatusCodesCode,
    )

    # End Import for CodeableConcept for paymentStatus


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class PaymentNotice(FhirResourceBase):
    """
    PaymentNotice
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: FinancialResourceStatusCodesCode,
        request: Optional[Reference[Union[Resource]]] = None,
        response: Optional[Reference[Union[Resource]]] = None,
        created: FhirDateTime,
        provider: Optional[
            Reference[Union[Practitioner, PractitionerRole, Organization]]
        ] = None,
        payment: Reference[Union[PaymentReconciliation]],
        paymentDate: Optional[FhirDate] = None,
        payee: Optional[
            Reference[Union[Practitioner, PractitionerRole, Organization]]
        ] = None,
        recipient: Reference[Union[Organization]],
        amount: Money,
        paymentStatus: Optional[CodeableConcept[PaymentStatusCodesCode]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: A unique identifier assigned to this payment notice.
            :param status: The status of the resource instance.
            :param request: Reference of resource for which payment is being made.
            :param response: Reference of response to resource for which payment is being made.
            :param created: The date when this resource was created.
            :param provider: The practitioner who is responsible for the services rendered to the patient.
            :param payment: A reference to the payment which is the subject of this notice.
            :param paymentDate: The date when the above payment action occurred.
            :param payee: The party who will receive or has received payment that is the subject of this
        notification.
            :param recipient: The party who is notified of the payment status.
            :param amount: The amount sent to the payee.
            :param paymentStatus: A code indicating whether payment has been sent or cleared.
        """
        super().__init__(
            resourceType="PaymentNotice",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            request=request,
            response=response,
            created=created,
            provider=provider,
            payment=payment,
            paymentDate=paymentDate,
            payee=payee,
            recipient=recipient,
            amount=amount,
            paymentStatus=paymentStatus,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return PaymentNoticeSchema.get_schema(include_extension=include_extension)
