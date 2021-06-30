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


class SchemaVersionList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, id):
        """
        Initialize the SchemaVersionList

        :param Version version: Version that contains the resource
        :param id: The unique identifier of the schema.

        :returns: twilio.rest.events.v1.schema.version.SchemaVersionList
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionList
        """
        super(SchemaVersionList, self).__init__(version)

        # Path Solution
        self._solution = {'id': id, }
        self._uri = '/Schemas/{id}/Versions'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams SchemaVersionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.events.v1.schema.version.SchemaVersionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SchemaVersionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.events.v1.schema.version.SchemaVersionInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SchemaVersionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SchemaVersionInstance
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return SchemaVersionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SchemaVersionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SchemaVersionInstance
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SchemaVersionPage(self._version, response, self._solution)

    def get(self, schema_version):
        """
        Constructs a SchemaVersionContext

        :param schema_version: The version of the schema

        :returns: twilio.rest.events.v1.schema.version.SchemaVersionContext
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionContext
        """
        return SchemaVersionContext(self._version, id=self._solution['id'], schema_version=schema_version, )

    def __call__(self, schema_version):
        """
        Constructs a SchemaVersionContext

        :param schema_version: The version of the schema

        :returns: twilio.rest.events.v1.schema.version.SchemaVersionContext
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionContext
        """
        return SchemaVersionContext(self._version, id=self._solution['id'], schema_version=schema_version, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1.SchemaVersionList>'


class SchemaVersionPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the SchemaVersionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param id: The unique identifier of the schema.

        :returns: twilio.rest.events.v1.schema.version.SchemaVersionPage
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionPage
        """
        super(SchemaVersionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SchemaVersionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.events.v1.schema.version.SchemaVersionInstance
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionInstance
        """
        return SchemaVersionInstance(self._version, payload, id=self._solution['id'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1.SchemaVersionPage>'


class SchemaVersionContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, id, schema_version):
        """
        Initialize the SchemaVersionContext

        :param Version version: Version that contains the resource
        :param id: The unique identifier of the schema.
        :param schema_version: The version of the schema

        :returns: twilio.rest.events.v1.schema.version.SchemaVersionContext
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionContext
        """
        super(SchemaVersionContext, self).__init__(version)

        # Path Solution
        self._solution = {'id': id, 'schema_version': schema_version, }
        self._uri = '/Schemas/{id}/Versions/{schema_version}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the SchemaVersionInstance

        :returns: The fetched SchemaVersionInstance
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SchemaVersionInstance(
            self._version,
            payload,
            id=self._solution['id'],
            schema_version=self._solution['schema_version'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.SchemaVersionContext {}>'.format(context)


class SchemaVersionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, id, schema_version=None):
        """
        Initialize the SchemaVersionInstance

        :returns: twilio.rest.events.v1.schema.version.SchemaVersionInstance
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionInstance
        """
        super(SchemaVersionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'id': payload.get('id'),
            'schema_version': deserialize.integer(payload.get('schema_version')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'url': payload.get('url'),
            'raw': payload.get('raw'),
        }

        # Context
        self._context = None
        self._solution = {'id': id, 'schema_version': schema_version or self._properties['schema_version'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SchemaVersionContext for this SchemaVersionInstance
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionContext
        """
        if self._context is None:
            self._context = SchemaVersionContext(
                self._version,
                id=self._solution['id'],
                schema_version=self._solution['schema_version'],
            )
        return self._context

    @property
    def id(self):
        """
        :returns: The unique identifier of the schema.
        :rtype: unicode
        """
        return self._properties['id']

    @property
    def schema_version(self):
        """
        :returns: The version of this schema.
        :rtype: unicode
        """
        return self._properties['schema_version']

    @property
    def date_created(self):
        """
        :returns: The date the schema version was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def raw(self):
        """
        :returns: The raw
        :rtype: unicode
        """
        return self._properties['raw']

    def fetch(self):
        """
        Fetch the SchemaVersionInstance

        :returns: The fetched SchemaVersionInstance
        :rtype: twilio.rest.events.v1.schema.version.SchemaVersionInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.SchemaVersionInstance {}>'.format(context)
