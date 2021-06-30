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


class CustomerProfilesEntityAssignmentsList(ListResource):

    def __init__(self, version, customer_profile_sid):
        """
        Initialize the CustomerProfilesEntityAssignmentsList

        :param Version version: Version that contains the resource
        :param customer_profile_sid: The unique string that identifies the CustomerProfile resource.

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsList
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsList
        """
        super(CustomerProfilesEntityAssignmentsList, self).__init__(version)

        # Path Solution
        self._solution = {'customer_profile_sid': customer_profile_sid, }
        self._uri = '/CustomerProfiles/{customer_profile_sid}/EntityAssignments'.format(**self._solution)

    def create(self, object_sid):
        """
        Create the CustomerProfilesEntityAssignmentsInstance

        :param unicode object_sid: The sid of an object bag

        :returns: The created CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance
        """
        data = values.of({'ObjectSid': object_sid, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return CustomerProfilesEntityAssignmentsInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution['customer_profile_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams CustomerProfilesEntityAssignmentsInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists CustomerProfilesEntityAssignmentsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of CustomerProfilesEntityAssignmentsInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return CustomerProfilesEntityAssignmentsPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CustomerProfilesEntityAssignmentsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CustomerProfilesEntityAssignmentsPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a CustomerProfilesEntityAssignmentsContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsContext
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsContext
        """
        return CustomerProfilesEntityAssignmentsContext(
            self._version,
            customer_profile_sid=self._solution['customer_profile_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a CustomerProfilesEntityAssignmentsContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsContext
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsContext
        """
        return CustomerProfilesEntityAssignmentsContext(
            self._version,
            customer_profile_sid=self._solution['customer_profile_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.CustomerProfilesEntityAssignmentsList>'


class CustomerProfilesEntityAssignmentsPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CustomerProfilesEntityAssignmentsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param customer_profile_sid: The unique string that identifies the CustomerProfile resource.

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsPage
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsPage
        """
        super(CustomerProfilesEntityAssignmentsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CustomerProfilesEntityAssignmentsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance
        """
        return CustomerProfilesEntityAssignmentsInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution['customer_profile_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.CustomerProfilesEntityAssignmentsPage>'


class CustomerProfilesEntityAssignmentsContext(InstanceContext):

    def __init__(self, version, customer_profile_sid, sid):
        """
        Initialize the CustomerProfilesEntityAssignmentsContext

        :param Version version: Version that contains the resource
        :param customer_profile_sid: The unique string that identifies the resource.
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsContext
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsContext
        """
        super(CustomerProfilesEntityAssignmentsContext, self).__init__(version)

        # Path Solution
        self._solution = {'customer_profile_sid': customer_profile_sid, 'sid': sid, }
        self._uri = '/CustomerProfiles/{customer_profile_sid}/EntityAssignments/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the CustomerProfilesEntityAssignmentsInstance

        :returns: The fetched CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CustomerProfilesEntityAssignmentsInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution['customer_profile_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the CustomerProfilesEntityAssignmentsInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.CustomerProfilesEntityAssignmentsContext {}>'.format(context)


class CustomerProfilesEntityAssignmentsInstance(InstanceResource):

    def __init__(self, version, payload, customer_profile_sid, sid=None):
        """
        Initialize the CustomerProfilesEntityAssignmentsInstance

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance
        """
        super(CustomerProfilesEntityAssignmentsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'customer_profile_sid': payload.get('customer_profile_sid'),
            'account_sid': payload.get('account_sid'),
            'object_sid': payload.get('object_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'customer_profile_sid': customer_profile_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CustomerProfilesEntityAssignmentsContext for this CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsContext
        """
        if self._context is None:
            self._context = CustomerProfilesEntityAssignmentsContext(
                self._version,
                customer_profile_sid=self._solution['customer_profile_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def customer_profile_sid(self):
        """
        :returns: The unique string that identifies the CustomerProfile resource.
        :rtype: unicode
        """
        return self._properties['customer_profile_sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def object_sid(self):
        """
        :returns: The sid of an object bag
        :rtype: unicode
        """
        return self._properties['object_sid']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Identity resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the CustomerProfilesEntityAssignmentsInstance

        :returns: The fetched CustomerProfilesEntityAssignmentsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_entity_assignments.CustomerProfilesEntityAssignmentsInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the CustomerProfilesEntityAssignmentsInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.CustomerProfilesEntityAssignmentsInstance {}>'.format(context)
