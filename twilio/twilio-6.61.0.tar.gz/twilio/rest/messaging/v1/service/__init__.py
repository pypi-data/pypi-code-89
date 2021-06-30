# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.messaging.v1.service.alpha_sender import AlphaSenderList
from twilio.rest.messaging.v1.service.phone_number import PhoneNumberList
from twilio.rest.messaging.v1.service.short_code import ShortCodeList
from twilio.rest.messaging.v1.service.us_app_to_person import UsAppToPersonList
from twilio.rest.messaging.v1.service.us_app_to_person_usecase import UsAppToPersonUsecaseList


class ServiceList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version):
        """
        Initialize the ServiceList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.messaging.v1.service.ServiceList
        :rtype: twilio.rest.messaging.v1.service.ServiceList
        """
        super(ServiceList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Services'.format(**self._solution)

    def create(self, friendly_name, inbound_request_url=values.unset,
               inbound_method=values.unset, fallback_url=values.unset,
               fallback_method=values.unset, status_callback=values.unset,
               sticky_sender=values.unset, mms_converter=values.unset,
               smart_encoding=values.unset, scan_message_content=values.unset,
               fallback_to_long_code=values.unset, area_code_geomatch=values.unset,
               validity_period=values.unset, synchronous_validation=values.unset,
               use_inbound_webhook_on_number=values.unset):
        """
        Create the ServiceInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode inbound_request_url: The URL we call using inbound_method when a message is received by any phone number or short code in the Service. This field will be overridden if the `use_inbound_webhook_on_number` field is enabled.
        :param unicode inbound_method: The HTTP method we should use to call inbound_request_url
        :param unicode fallback_url: The URL that we call using fallback_method if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. This field will be overridden if the `use_inbound_webhook_on_number` field is enabled.
        :param unicode fallback_method: The HTTP method we should use to call fallback_url
        :param unicode status_callback: The URL we should call to pass status updates about message delivery
        :param bool sticky_sender: Whether to enable Sticky Sender on the Service instance
        :param bool mms_converter: Whether to enable the MMS Converter for messages sent through the Service instance
        :param bool smart_encoding: Whether to enable Encoding for messages sent through the Service instance
        :param ServiceInstance.ScanMessageContent scan_message_content: Reserved
        :param bool fallback_to_long_code: Whether to enable Fallback to Long Code for messages sent through the Service instance
        :param bool area_code_geomatch: Whether to enable Area Code Geomatch on the Service Instance
        :param unicode validity_period: How long, in seconds, messages sent from the Service are valid
        :param bool synchronous_validation: Reserved
        :param bool use_inbound_webhook_on_number: If enabled, the webhook url configured on the phone number will be used and will override the `inbound_request_url`/`fallback_url` url called when an inbound message is received.

        :returns: The created ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'InboundRequestUrl': inbound_request_url,
            'InboundMethod': inbound_method,
            'FallbackUrl': fallback_url,
            'FallbackMethod': fallback_method,
            'StatusCallback': status_callback,
            'StickySender': sticky_sender,
            'MmsConverter': mms_converter,
            'SmartEncoding': smart_encoding,
            'ScanMessageContent': scan_message_content,
            'FallbackToLongCode': fallback_to_long_code,
            'AreaCodeGeomatch': area_code_geomatch,
            'ValidityPeriod': validity_period,
            'SynchronousValidation': synchronous_validation,
            'UseInboundWebhookOnNumber': use_inbound_webhook_on_number,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return ServiceInstance(self._version, payload, )

    def stream(self, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.service.ServiceInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServicePage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return ServicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ServicePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ServiceContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.service.ServiceContext
        :rtype: twilio.rest.messaging.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ServiceContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.service.ServiceContext
        :rtype: twilio.rest.messaging.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.ServiceList>'


class ServicePage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the ServicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.messaging.v1.service.ServicePage
        :rtype: twilio.rest.messaging.v1.service.ServicePage
        """
        super(ServicePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.service.ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.ServicePage>'


class ServiceContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, sid):
        """
        Initialize the ServiceContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.messaging.v1.service.ServiceContext
        :rtype: twilio.rest.messaging.v1.service.ServiceContext
        """
        super(ServiceContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Services/{sid}'.format(**self._solution)

        # Dependents
        self._phone_numbers = None
        self._short_codes = None
        self._alpha_senders = None
        self._us_app_to_person = None
        self._us_app_to_person_usecases = None

    def update(self, friendly_name=values.unset, inbound_request_url=values.unset,
               inbound_method=values.unset, fallback_url=values.unset,
               fallback_method=values.unset, status_callback=values.unset,
               sticky_sender=values.unset, mms_converter=values.unset,
               smart_encoding=values.unset, scan_message_content=values.unset,
               fallback_to_long_code=values.unset, area_code_geomatch=values.unset,
               validity_period=values.unset, synchronous_validation=values.unset,
               use_inbound_webhook_on_number=values.unset):
        """
        Update the ServiceInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode inbound_request_url: The URL we call using inbound_method when a message is received by any phone number or short code in the Service. This field will be overridden if the `use_inbound_webhook_on_number` field is enabled.
        :param unicode inbound_method: The HTTP method we should use to call inbound_request_url
        :param unicode fallback_url: The URL that we call using fallback_method if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. This field will be overridden if the `use_inbound_webhook_on_number` field is enabled.
        :param unicode fallback_method: The HTTP method we should use to call fallback_url
        :param unicode status_callback: The URL we should call to pass status updates about message delivery
        :param bool sticky_sender: Whether to enable Sticky Sender on the Service instance
        :param bool mms_converter: Whether to enable the MMS Converter for messages sent through the Service instance
        :param bool smart_encoding: Whether to enable Encoding for messages sent through the Service instance
        :param ServiceInstance.ScanMessageContent scan_message_content: Reserved
        :param bool fallback_to_long_code: Whether to enable Fallback to Long Code for messages sent through the Service instance
        :param bool area_code_geomatch: Whether to enable Area Code Geomatch on the Service Instance
        :param unicode validity_period: How long, in seconds, messages sent from the Service are valid
        :param bool synchronous_validation: Reserved
        :param bool use_inbound_webhook_on_number: If enabled, the webhook url configured on the phone number will be used and will override the `inbound_request_url`/`fallback_url` url called when an inbound message is received.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'InboundRequestUrl': inbound_request_url,
            'InboundMethod': inbound_method,
            'FallbackUrl': fallback_url,
            'FallbackMethod': fallback_method,
            'StatusCallback': status_callback,
            'StickySender': sticky_sender,
            'MmsConverter': mms_converter,
            'SmartEncoding': smart_encoding,
            'ScanMessageContent': scan_message_content,
            'FallbackToLongCode': fallback_to_long_code,
            'AreaCodeGeomatch': area_code_geomatch,
            'ValidityPeriod': validity_period,
            'SynchronousValidation': synchronous_validation,
            'UseInboundWebhookOnNumber': use_inbound_webhook_on_number,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return ServiceInstance(self._version, payload, sid=self._solution['sid'], )

    def fetch(self):
        """
        Fetch the ServiceInstance

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ServiceInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the ServiceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    @property
    def phone_numbers(self):
        """
        Access the phone_numbers

        :returns: twilio.rest.messaging.v1.service.phone_number.PhoneNumberList
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberList
        """
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberList(self._version, service_sid=self._solution['sid'], )
        return self._phone_numbers

    @property
    def short_codes(self):
        """
        Access the short_codes

        :returns: twilio.rest.messaging.v1.service.short_code.ShortCodeList
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeList
        """
        if self._short_codes is None:
            self._short_codes = ShortCodeList(self._version, service_sid=self._solution['sid'], )
        return self._short_codes

    @property
    def alpha_senders(self):
        """
        Access the alpha_senders

        :returns: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderList
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderList
        """
        if self._alpha_senders is None:
            self._alpha_senders = AlphaSenderList(self._version, service_sid=self._solution['sid'], )
        return self._alpha_senders

    @property
    def us_app_to_person(self):
        """
        Access the us_app_to_person

        :returns: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonList
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonList
        """
        if self._us_app_to_person is None:
            self._us_app_to_person = UsAppToPersonList(
                self._version,
                messaging_service_sid=self._solution['sid'],
            )
        return self._us_app_to_person

    @property
    def us_app_to_person_usecases(self):
        """
        Access the us_app_to_person_usecases

        :returns: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecaseList
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecaseList
        """
        if self._us_app_to_person_usecases is None:
            self._us_app_to_person_usecases = UsAppToPersonUsecaseList(
                self._version,
                messaging_service_sid=self._solution['sid'],
            )
        return self._us_app_to_person_usecases

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.ServiceContext {}>'.format(context)


class ServiceInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class ScanMessageContent(object):
        INHERIT = "inherit"
        ENABLE = "enable"
        DISABLE = "disable"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the ServiceInstance

        :returns: twilio.rest.messaging.v1.service.ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        super(ServiceInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'inbound_request_url': payload.get('inbound_request_url'),
            'inbound_method': payload.get('inbound_method'),
            'fallback_url': payload.get('fallback_url'),
            'fallback_method': payload.get('fallback_method'),
            'status_callback': payload.get('status_callback'),
            'sticky_sender': payload.get('sticky_sender'),
            'mms_converter': payload.get('mms_converter'),
            'smart_encoding': payload.get('smart_encoding'),
            'scan_message_content': payload.get('scan_message_content'),
            'fallback_to_long_code': payload.get('fallback_to_long_code'),
            'area_code_geomatch': payload.get('area_code_geomatch'),
            'synchronous_validation': payload.get('synchronous_validation'),
            'validity_period': deserialize.integer(payload.get('validity_period')),
            'url': payload.get('url'),
            'links': payload.get('links'),
            'use_inbound_webhook_on_number': payload.get('use_inbound_webhook_on_number'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceContext
        """
        if self._context is None:
            self._context = ServiceContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def inbound_request_url(self):
        """
        :returns: The URL we call using inbound_method when a message is received by any phone number or short code in the Service. This field will be overridden if the `use_inbound_webhook_on_number` field is enabled.
        :rtype: unicode
        """
        return self._properties['inbound_request_url']

    @property
    def inbound_method(self):
        """
        :returns: The HTTP method we use to call inbound_request_url
        :rtype: unicode
        """
        return self._properties['inbound_method']

    @property
    def fallback_url(self):
        """
        :returns: The URL that we call using fallback_method if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. This field will be overridden if the `use_inbound_webhook_on_number` field is enabled.
        :rtype: unicode
        """
        return self._properties['fallback_url']

    @property
    def fallback_method(self):
        """
        :returns: The HTTP method we use to call fallback_url
        :rtype: unicode
        """
        return self._properties['fallback_method']

    @property
    def status_callback(self):
        """
        :returns: The URL we call to pass status updates about message delivery
        :rtype: unicode
        """
        return self._properties['status_callback']

    @property
    def sticky_sender(self):
        """
        :returns: Whether to enable Sticky Sender on the Service instance
        :rtype: bool
        """
        return self._properties['sticky_sender']

    @property
    def mms_converter(self):
        """
        :returns: Whether to enable the MMS Converter for messages sent through the Service instance
        :rtype: bool
        """
        return self._properties['mms_converter']

    @property
    def smart_encoding(self):
        """
        :returns: Whether to enable Encoding for messages sent through the Service instance
        :rtype: bool
        """
        return self._properties['smart_encoding']

    @property
    def scan_message_content(self):
        """
        :returns: Reserved
        :rtype: ServiceInstance.ScanMessageContent
        """
        return self._properties['scan_message_content']

    @property
    def fallback_to_long_code(self):
        """
        :returns: Whether to enable Fallback to Long Code for messages sent through the Service instance
        :rtype: bool
        """
        return self._properties['fallback_to_long_code']

    @property
    def area_code_geomatch(self):
        """
        :returns: Whether to enable Area Code Geomatch on the Service Instance
        :rtype: bool
        """
        return self._properties['area_code_geomatch']

    @property
    def synchronous_validation(self):
        """
        :returns: Reserved
        :rtype: bool
        """
        return self._properties['synchronous_validation']

    @property
    def validity_period(self):
        """
        :returns: How long, in seconds, messages sent from the Service are valid
        :rtype: unicode
        """
        return self._properties['validity_period']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Service resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The absolute URLs of related resources
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def use_inbound_webhook_on_number(self):
        """
        :returns: If enabled, the webhook url configured on the phone number will be used and will override the `inbound_request_url`/`fallback_url` url called when an inbound message is received.
        :rtype: bool
        """
        return self._properties['use_inbound_webhook_on_number']

    def update(self, friendly_name=values.unset, inbound_request_url=values.unset,
               inbound_method=values.unset, fallback_url=values.unset,
               fallback_method=values.unset, status_callback=values.unset,
               sticky_sender=values.unset, mms_converter=values.unset,
               smart_encoding=values.unset, scan_message_content=values.unset,
               fallback_to_long_code=values.unset, area_code_geomatch=values.unset,
               validity_period=values.unset, synchronous_validation=values.unset,
               use_inbound_webhook_on_number=values.unset):
        """
        Update the ServiceInstance

        :param unicode friendly_name: A string to describe the resource
        :param unicode inbound_request_url: The URL we call using inbound_method when a message is received by any phone number or short code in the Service. This field will be overridden if the `use_inbound_webhook_on_number` field is enabled.
        :param unicode inbound_method: The HTTP method we should use to call inbound_request_url
        :param unicode fallback_url: The URL that we call using fallback_method if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. This field will be overridden if the `use_inbound_webhook_on_number` field is enabled.
        :param unicode fallback_method: The HTTP method we should use to call fallback_url
        :param unicode status_callback: The URL we should call to pass status updates about message delivery
        :param bool sticky_sender: Whether to enable Sticky Sender on the Service instance
        :param bool mms_converter: Whether to enable the MMS Converter for messages sent through the Service instance
        :param bool smart_encoding: Whether to enable Encoding for messages sent through the Service instance
        :param ServiceInstance.ScanMessageContent scan_message_content: Reserved
        :param bool fallback_to_long_code: Whether to enable Fallback to Long Code for messages sent through the Service instance
        :param bool area_code_geomatch: Whether to enable Area Code Geomatch on the Service Instance
        :param unicode validity_period: How long, in seconds, messages sent from the Service are valid
        :param bool synchronous_validation: Reserved
        :param bool use_inbound_webhook_on_number: If enabled, the webhook url configured on the phone number will be used and will override the `inbound_request_url`/`fallback_url` url called when an inbound message is received.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            inbound_request_url=inbound_request_url,
            inbound_method=inbound_method,
            fallback_url=fallback_url,
            fallback_method=fallback_method,
            status_callback=status_callback,
            sticky_sender=sticky_sender,
            mms_converter=mms_converter,
            smart_encoding=smart_encoding,
            scan_message_content=scan_message_content,
            fallback_to_long_code=fallback_to_long_code,
            area_code_geomatch=area_code_geomatch,
            validity_period=validity_period,
            synchronous_validation=synchronous_validation,
            use_inbound_webhook_on_number=use_inbound_webhook_on_number,
        )

    def fetch(self):
        """
        Fetch the ServiceInstance

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the ServiceInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def phone_numbers(self):
        """
        Access the phone_numbers

        :returns: twilio.rest.messaging.v1.service.phone_number.PhoneNumberList
        :rtype: twilio.rest.messaging.v1.service.phone_number.PhoneNumberList
        """
        return self._proxy.phone_numbers

    @property
    def short_codes(self):
        """
        Access the short_codes

        :returns: twilio.rest.messaging.v1.service.short_code.ShortCodeList
        :rtype: twilio.rest.messaging.v1.service.short_code.ShortCodeList
        """
        return self._proxy.short_codes

    @property
    def alpha_senders(self):
        """
        Access the alpha_senders

        :returns: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderList
        :rtype: twilio.rest.messaging.v1.service.alpha_sender.AlphaSenderList
        """
        return self._proxy.alpha_senders

    @property
    def us_app_to_person(self):
        """
        Access the us_app_to_person

        :returns: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonList
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonList
        """
        return self._proxy.us_app_to_person

    @property
    def us_app_to_person_usecases(self):
        """
        Access the us_app_to_person_usecases

        :returns: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecaseList
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person_usecase.UsAppToPersonUsecaseList
        """
        return self._proxy.us_app_to_person_usecases

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.ServiceInstance {}>'.format(context)
