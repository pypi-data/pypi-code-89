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
from twilio.rest.preview.deployed_devices.fleet.certificate import CertificateList
from twilio.rest.preview.deployed_devices.fleet.deployment import DeploymentList
from twilio.rest.preview.deployed_devices.fleet.device import DeviceList
from twilio.rest.preview.deployed_devices.fleet.key import KeyList


class FleetList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the FleetList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetList
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetList
        """
        super(FleetList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Fleets'.format(**self._solution)

    def create(self, friendly_name=values.unset):
        """
        Create the FleetInstance

        :param unicode friendly_name: A human readable description for this Fleet.

        :returns: The created FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        data = values.of({'FriendlyName': friendly_name, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return FleetInstance(self._version, payload, )

    def stream(self, limit=None, page_size=None):
        """
        Streams FleetInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.FleetInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FleetInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.FleetInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of FleetInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return FleetPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FleetInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return FleetPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a FleetContext

        :param sid: A string that uniquely identifies the Fleet.

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetContext
        """
        return FleetContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a FleetContext

        :param sid: A string that uniquely identifies the Fleet.

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetContext
        """
        return FleetContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.FleetList>'


class FleetPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the FleetPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetPage
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetPage
        """
        super(FleetPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FleetInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        return FleetInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.FleetPage>'


class FleetContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the FleetContext

        :param Version version: Version that contains the resource
        :param sid: A string that uniquely identifies the Fleet.

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetContext
        """
        super(FleetContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Fleets/{sid}'.format(**self._solution)

        # Dependents
        self._devices = None
        self._deployments = None
        self._certificates = None
        self._keys = None

    def fetch(self):
        """
        Fetch the FleetInstance

        :returns: The fetched FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FleetInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the FleetInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def update(self, friendly_name=values.unset,
               default_deployment_sid=values.unset):
        """
        Update the FleetInstance

        :param unicode friendly_name: A human readable description for this Fleet.
        :param unicode default_deployment_sid: A default Deployment SID.

        :returns: The updated FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        data = values.of({'FriendlyName': friendly_name, 'DefaultDeploymentSid': default_deployment_sid, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return FleetInstance(self._version, payload, sid=self._solution['sid'], )

    @property
    def devices(self):
        """
        Access the devices

        :returns: twilio.rest.preview.deployed_devices.fleet.device.DeviceList
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceList
        """
        if self._devices is None:
            self._devices = DeviceList(self._version, fleet_sid=self._solution['sid'], )
        return self._devices

    @property
    def deployments(self):
        """
        Access the deployments

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentList
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentList
        """
        if self._deployments is None:
            self._deployments = DeploymentList(self._version, fleet_sid=self._solution['sid'], )
        return self._deployments

    @property
    def certificates(self):
        """
        Access the certificates

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateList
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateList
        """
        if self._certificates is None:
            self._certificates = CertificateList(self._version, fleet_sid=self._solution['sid'], )
        return self._certificates

    @property
    def keys(self):
        """
        Access the keys

        :returns: twilio.rest.preview.deployed_devices.fleet.key.KeyList
        :rtype: twilio.rest.preview.deployed_devices.fleet.key.KeyList
        """
        if self._keys is None:
            self._keys = KeyList(self._version, fleet_sid=self._solution['sid'], )
        return self._keys

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.FleetContext {}>'.format(context)


class FleetInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, sid=None):
        """
        Initialize the FleetInstance

        :returns: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        super(FleetInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'url': payload.get('url'),
            'unique_name': payload.get('unique_name'),
            'friendly_name': payload.get('friendly_name'),
            'account_sid': payload.get('account_sid'),
            'default_deployment_sid': payload.get('default_deployment_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FleetContext for this FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetContext
        """
        if self._context is None:
            self._context = FleetContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Fleet.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def url(self):
        """
        :returns: URL of this Fleet.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def unique_name(self):
        """
        :returns: A unique, addressable name of this Fleet.
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description for this Fleet.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def account_sid(self):
        """
        :returns: The unique SID that identifies this Account.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def default_deployment_sid(self):
        """
        :returns: The unique SID that identifies this Fleet's default Deployment.
        :rtype: unicode
        """
        return self._properties['default_deployment_sid']

    @property
    def date_created(self):
        """
        :returns: The date this Fleet was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Fleet was updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def links(self):
        """
        :returns: Nested resource URLs.
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the FleetInstance

        :returns: The fetched FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the FleetInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, friendly_name=values.unset,
               default_deployment_sid=values.unset):
        """
        Update the FleetInstance

        :param unicode friendly_name: A human readable description for this Fleet.
        :param unicode default_deployment_sid: A default Deployment SID.

        :returns: The updated FleetInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.FleetInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            default_deployment_sid=default_deployment_sid,
        )

    @property
    def devices(self):
        """
        Access the devices

        :returns: twilio.rest.preview.deployed_devices.fleet.device.DeviceList
        :rtype: twilio.rest.preview.deployed_devices.fleet.device.DeviceList
        """
        return self._proxy.devices

    @property
    def deployments(self):
        """
        Access the deployments

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentList
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentList
        """
        return self._proxy.deployments

    @property
    def certificates(self):
        """
        Access the certificates

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateList
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateList
        """
        return self._proxy.certificates

    @property
    def keys(self):
        """
        Access the keys

        :returns: twilio.rest.preview.deployed_devices.fleet.key.KeyList
        :rtype: twilio.rest.preview.deployed_devices.fleet.key.KeyList
        """
        return self._proxy.keys

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.FleetInstance {}>'.format(context)
