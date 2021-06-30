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


class CustomerProfilesEvaluationsList(ListResource):

    def __init__(self, version, customer_profile_sid):
        """
        Initialize the CustomerProfilesEvaluationsList

        :param Version version: Version that contains the resource
        :param customer_profile_sid: The unique string that identifies the resource

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsList
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsList
        """
        super(CustomerProfilesEvaluationsList, self).__init__(version)

        # Path Solution
        self._solution = {'customer_profile_sid': customer_profile_sid, }
        self._uri = '/CustomerProfiles/{customer_profile_sid}/Evaluations'.format(**self._solution)

    def create(self, policy_sid):
        """
        Create the CustomerProfilesEvaluationsInstance

        :param unicode policy_sid: The unique string of a policy

        :returns: The created CustomerProfilesEvaluationsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsInstance
        """
        data = values.of({'PolicySid': policy_sid, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return CustomerProfilesEvaluationsInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution['customer_profile_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams CustomerProfilesEvaluationsInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists CustomerProfilesEvaluationsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of CustomerProfilesEvaluationsInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CustomerProfilesEvaluationsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return CustomerProfilesEvaluationsPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CustomerProfilesEvaluationsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CustomerProfilesEvaluationsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CustomerProfilesEvaluationsPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a CustomerProfilesEvaluationsContext

        :param sid: The unique string that identifies the Evaluation resource

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsContext
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsContext
        """
        return CustomerProfilesEvaluationsContext(
            self._version,
            customer_profile_sid=self._solution['customer_profile_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a CustomerProfilesEvaluationsContext

        :param sid: The unique string that identifies the Evaluation resource

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsContext
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsContext
        """
        return CustomerProfilesEvaluationsContext(
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
        return '<Twilio.Trusthub.V1.CustomerProfilesEvaluationsList>'


class CustomerProfilesEvaluationsPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CustomerProfilesEvaluationsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param customer_profile_sid: The unique string that identifies the resource

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsPage
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsPage
        """
        super(CustomerProfilesEvaluationsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CustomerProfilesEvaluationsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsInstance
        """
        return CustomerProfilesEvaluationsInstance(
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
        return '<Twilio.Trusthub.V1.CustomerProfilesEvaluationsPage>'


class CustomerProfilesEvaluationsContext(InstanceContext):

    def __init__(self, version, customer_profile_sid, sid):
        """
        Initialize the CustomerProfilesEvaluationsContext

        :param Version version: Version that contains the resource
        :param customer_profile_sid: The unique string that identifies the resource
        :param sid: The unique string that identifies the Evaluation resource

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsContext
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsContext
        """
        super(CustomerProfilesEvaluationsContext, self).__init__(version)

        # Path Solution
        self._solution = {'customer_profile_sid': customer_profile_sid, 'sid': sid, }
        self._uri = '/CustomerProfiles/{customer_profile_sid}/Evaluations/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the CustomerProfilesEvaluationsInstance

        :returns: The fetched CustomerProfilesEvaluationsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CustomerProfilesEvaluationsInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution['customer_profile_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.CustomerProfilesEvaluationsContext {}>'.format(context)


class CustomerProfilesEvaluationsInstance(InstanceResource):

    class Status(object):
        COMPLIANT = "compliant"
        NONCOMPLIANT = "noncompliant"

    def __init__(self, version, payload, customer_profile_sid, sid=None):
        """
        Initialize the CustomerProfilesEvaluationsInstance

        :returns: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsInstance
        """
        super(CustomerProfilesEvaluationsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'policy_sid': payload.get('policy_sid'),
            'customer_profile_sid': payload.get('customer_profile_sid'),
            'status': payload.get('status'),
            'results': payload.get('results'),
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

        :returns: CustomerProfilesEvaluationsContext for this CustomerProfilesEvaluationsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsContext
        """
        if self._context is None:
            self._context = CustomerProfilesEvaluationsContext(
                self._version,
                customer_profile_sid=self._solution['customer_profile_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the Evaluation resource
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
    def policy_sid(self):
        """
        :returns: The unique string of a policy
        :rtype: unicode
        """
        return self._properties['policy_sid']

    @property
    def customer_profile_sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['customer_profile_sid']

    @property
    def status(self):
        """
        :returns: The compliance status of the Evaluation resource
        :rtype: CustomerProfilesEvaluationsInstance.Status
        """
        return self._properties['status']

    @property
    def results(self):
        """
        :returns: The results of the Evaluation resource
        :rtype: list[dict]
        """
        return self._properties['results']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the CustomerProfilesEvaluationsInstance

        :returns: The fetched CustomerProfilesEvaluationsInstance
        :rtype: twilio.rest.trusthub.v1.customer_profiles.customer_profiles_evaluations.CustomerProfilesEvaluationsInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.CustomerProfilesEvaluationsInstance {}>'.format(context)
