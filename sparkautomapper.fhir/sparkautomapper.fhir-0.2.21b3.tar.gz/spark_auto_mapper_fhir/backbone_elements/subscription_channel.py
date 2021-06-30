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
    # type_ (SubscriptionChannelType)
    from spark_auto_mapper_fhir.value_sets.subscription_channel_type import (
        SubscriptionChannelTypeCode,
    )

    # endpoint (url)
    from spark_auto_mapper_fhir.complex_types.url import url

    # payload (Mime Types)
    from spark_auto_mapper_fhir.value_sets.mime_types import MimeTypesCode

    # header (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class SubscriptionChannel(FhirBackboneElementBase):
    """
    Subscription.Channel
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type_: SubscriptionChannelTypeCode,
        endpoint: Optional[url] = None,
        payload: Optional[MimeTypesCode] = None,
        header: Optional[FhirList[FhirString]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param type_: The type of channel to send notifications on.
            :param endpoint: The url that describes the actual end-point to send messages to.
            :param payload: The mime type to send the payload in - either application/fhir+xml, or
        application/fhir+json. If the payload is not present, then there is no payload
        in the notification, just a notification. The mime type "text/plain" may also
        be used for Email and SMS subscriptions.
            :param header: Additional headers / information to send as part of the notification.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            endpoint=endpoint,
            payload=payload,
            header=header,
        )
