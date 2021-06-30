# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class NotificationList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, identity, challenge_sid):
        """
        Initialize the NotificationList

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.
        :param identity: Unique external identifier of the Entity
        :param challenge_sid: Challenge Sid.

        :returns: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationList
        :rtype: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationList
        """
        super(NotificationList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'identity': identity, 'challenge_sid': challenge_sid, }
        self._uri = '/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications'.format(**self._solution)

    def create(self, ttl=values.unset):
        """
        Create the NotificationInstance

        :param unicode ttl: How long, in seconds, the notification is valid.

        :returns: The created NotificationInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationInstance
        """
        data = values.of({'Ttl': ttl, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return NotificationInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            challenge_sid=self._solution['challenge_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.NotificationList>'


class NotificationPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the NotificationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Sid.
        :param identity: Unique external identifier of the Entity
        :param challenge_sid: Challenge Sid.

        :returns: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationPage
        :rtype: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationPage
        """
        super(NotificationPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NotificationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationInstance
        """
        return NotificationInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            challenge_sid=self._solution['challenge_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.NotificationPage>'


class NotificationInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, identity, challenge_sid):
        """
        Initialize the NotificationInstance

        :returns: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationInstance
        """
        super(NotificationInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'entity_sid': payload.get('entity_sid'),
            'identity': payload.get('identity'),
            'challenge_sid': payload.get('challenge_sid'),
            'priority': payload.get('priority'),
            'ttl': deserialize.integer(payload.get('ttl')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'identity': identity, 'challenge_sid': challenge_sid, }

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Notification.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: Service Sid.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def entity_sid(self):
        """
        :returns: Entity Sid.
        :rtype: unicode
        """
        return self._properties['entity_sid']

    @property
    def identity(self):
        """
        :returns: Unique external identifier of the Entity
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def challenge_sid(self):
        """
        :returns: Challenge Sid.
        :rtype: unicode
        """
        return self._properties['challenge_sid']

    @property
    def priority(self):
        """
        :returns: The priority of the notification.
        :rtype: unicode
        """
        return self._properties['priority']

    @property
    def ttl(self):
        """
        :returns: How long, in seconds, the notification is valid.
        :rtype: unicode
        """
        return self._properties['ttl']

    @property
    def date_created(self):
        """
        :returns: The date this Notification was created
        :rtype: datetime
        """
        return self._properties['date_created']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.NotificationInstance>'
