# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class EventList(ListResource):

    def __init__(self, version, account_sid, call_sid):
        """
        Initialize the EventList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created this resource
        :param call_sid: The unique string that identifies this resource

        :returns: twilio.rest.api.v2010.account.call.event.EventList
        :rtype: twilio.rest.api.v2010.account.call.event.EventList
        """
        super(EventList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'call_sid': call_sid, }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Events.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams EventInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.call.event.EventInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists EventInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.call.event.EventInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of EventInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EventInstance
        :rtype: twilio.rest.api.v2010.account.call.event.EventPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return EventPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EventInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EventInstance
        :rtype: twilio.rest.api.v2010.account.call.event.EventPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return EventPage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.EventList>'


class EventPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the EventPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created this resource
        :param call_sid: The unique string that identifies this resource

        :returns: twilio.rest.api.v2010.account.call.event.EventPage
        :rtype: twilio.rest.api.v2010.account.call.event.EventPage
        """
        super(EventPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EventInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.call.event.EventInstance
        :rtype: twilio.rest.api.v2010.account.call.event.EventInstance
        """
        return EventInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.EventPage>'


class EventInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, call_sid):
        """
        Initialize the EventInstance

        :returns: twilio.rest.api.v2010.account.call.event.EventInstance
        :rtype: twilio.rest.api.v2010.account.call.event.EventInstance
        """
        super(EventInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {'request': payload.get('request'), 'response': payload.get('response'), }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'call_sid': call_sid, }

    @property
    def request(self):
        """
        :returns: Call Request.
        :rtype: dict
        """
        return self._properties['request']

    @property
    def response(self):
        """
        :returns: Call Response with Events.
        :rtype: dict
        """
        return self._properties['response']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.EventInstance>'
