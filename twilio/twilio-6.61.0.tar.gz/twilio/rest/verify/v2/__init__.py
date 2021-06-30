# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.verify.v2.form import FormList
from twilio.rest.verify.v2.service import ServiceList
from twilio.rest.verify.v2.verification_attempt import VerificationAttemptList


class V2(Version):

    def __init__(self, domain):
        """
        Initialize the V2 version of Verify

        :returns: V2 version of Verify
        :rtype: twilio.rest.verify.v2.V2.V2
        """
        super(V2, self).__init__(domain)
        self.version = 'v2'
        self._forms = None
        self._services = None
        self._verification_attempts = None

    @property
    def forms(self):
        """
        :rtype: twilio.rest.verify.v2.form.FormList
        """
        if self._forms is None:
            self._forms = FormList(self)
        return self._forms

    @property
    def services(self):
        """
        :rtype: twilio.rest.verify.v2.service.ServiceList
        """
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    @property
    def verification_attempts(self):
        """
        :rtype: twilio.rest.verify.v2.verification_attempt.VerificationAttemptList
        """
        if self._verification_attempts is None:
            self._verification_attempts = VerificationAttemptList(self)
        return self._verification_attempts

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2>'
