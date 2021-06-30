"""
This is the SMTP server functionality for Mailrise.
"""

from __future__ import annotations

import asyncio
import email.policy
import functools
import os
import re
import typing as typ
from asyncio import get_running_loop
from dataclasses import dataclass
from email.message import EmailMessage
from email.parser import BytesParser
from email.utils import parseaddr
from tempfile import NamedTemporaryFile

from mailrise.config import MailriseConfig

import apprise  # type: ignore
from apprise.attachment import AttachBase  # type: ignore
from apprise.common import ContentLocation  # type: ignore
from aiosmtpd.smtp import Envelope, Session, SMTP


class RecipientError(Exception):
    """Exception raised for invalid recipient email addresses.

    Attributes:
        message: The reason the recipient is invalid.
    """
    message: str

    def __init__(self, message: str) -> None:
        self.message = message


class AppriseNotifyFailure(Exception):
    """Exception raised when Apprise fails to deliver a notification.

    Note: Apprise does not provide any information about the reason for the
    failure."""
    pass


@dataclass
class Recipient:
    """The routing information encoded into a recipient address.

    Attributes:
        config_key: An index into the `configs` dictionary.
        notify_type: The type of notification to send.
    """
    config_key: str
    notify_type: apprise.NotifyType


def parsercpt(addr: str) -> Recipient:
    """Parses an email address into a `Recipient`.

    Args:
        addr: The email address to parse.

    Returns:
        The `Recipient` instance.
    """
    _, email = parseaddr(addr)
    rx_types = r'((?:\.(?:info|success|warning|failure))?)'
    rx = f'(?:"([^"@\\.]*){rx_types}"|([^@\\.]*){rx_types})@mailrise\\.xyz$'
    match = re.search(rx, email, re.IGNORECASE)
    if match is None:
        raise RecipientError(f"'{email}' is not a valid mailrise recipient")
    quoted = match.group(1) is not None
    key = match.group(1) if quoted else match.group(3)
    ntypes = (match.group(2) if quoted else match.group(4)).lower()

    ntype = apprise.NotifyType.INFO
    if ntypes == '.info':
        pass
    elif ntypes == '.success':
        ntype = apprise.NotifyType.SUCCESS
    elif ntypes == '.warning':
        ntype = apprise.NotifyType.WARNING
    elif ntypes == '.failure':
        ntype = apprise.NotifyType.FAILURE

    return Recipient(config_key=key, notify_type=ntype)


@dataclass
class AppriseHandler:
    """The aiosmtpd handler for Mailrise. Dispatches Apprise notifications.

    Attributes:
        config: This server's Mailrise configuration.
    """
    config: MailriseConfig

    async def handle_RCPT(self, server: SMTP, session: Session, envelope: Envelope,
                          address: str, rcpt_options: list[str]) -> str:
        try:
            rcpt = parsercpt(address)
        except RecipientError as e:
            return f'550 {e.message}'
        if rcpt.config_key not in self.config.senders:
            return '551 recipient does not exist in configuration file'
        self.config.logger.info('Accepted recipient: %s', address)
        envelope.rcpt_tos.append(address)
        return '250 OK'

    async def handle_DATA(self, server: SMTP, session: Session, envelope: Envelope) \
            -> str:
        assert isinstance(envelope.content, bytes)
        parser = BytesParser(policy=email.policy.default)
        message = parser.parsebytes(envelope.content)
        assert isinstance(message, EmailMessage)
        notification = parsemessage(message)
        self.config.logger.info('Accepted email, subject: %s', notification.title)

        rcpts = (parsercpt(addr) for addr in envelope.rcpt_tos)
        aws = (notification.submit(self.config, rcpt) for rcpt in rcpts)
        try:
            await asyncio.gather(*aws)
        except AppriseNotifyFailure:
            return '450 failed to send notification'
        return '250 OK'


@dataclass
class Attachment:
    """Represents an email attachment.

    Attributes:
        data: The contents of the attachment.
        filename: The filename of the attachment as it was set by the sender.
    """
    data: bytes
    filename: str


@dataclass
class EmailNotification:
    """A notification template that has been constructed from an email message.

    Attributes:
        title: The title of the notification.
        body: The contents of the notification.
        body_format: The type of the contents of the notification.
        attachments: The attachments attached to the notification.
    """
    title: str
    body: str
    body_format: apprise.NotifyFormat
    attachments: list[Attachment]

    async def submit(self, config: MailriseConfig, rcpt: Recipient) -> None:
        """Turns the email into an Apprise notification and submits it.

        Args:
            config: The Mailrise configuration to use.
            rcpt: The recipient data to use.

        Raises:
            AppriseNotifyFailure: Apprise failed to submit the notification.
        """
        apobj = config.senders[rcpt.config_key]
        attachbase = [AttachMailrise(config, attach) for attach in self.attachments]
        notify = functools.partial(
            apobj.notify,
            title=self.title,
            body=self.body,
            body_format=self.body_format,
            notify_type=rcpt.notify_type,
            attach=apprise.AppriseAttachment(attachbase)
        )
        res = await get_running_loop().run_in_executor(None, notify)
        # NOTE: This should probably be called by Apprise itself, but it isn't?
        for ab in attachbase:
            ab.invalidate()
        if not res:
            raise AppriseNotifyFailure()


def parsemessage(msg: EmailMessage) -> EmailNotification:
    """Parses an email message into an `EmailNotification`.

    Args:
        msg: The email message.

    Returns:
        The `EmailNotification` instance.
    """
    subject = msg.get('Subject', '(no subject)')
    sender = msg.get('From', None)
    title = f'{subject} ({sender})' if sender else f'{subject} (no sender)'
    body_part = msg.get_body()
    body: str
    body_format: apprise.NotifyFormat
    if isinstance(body_part, EmailMessage):
        body = body_part.get_content().strip()
        body_format = \
            (apprise.NotifyFormat.HTML if body_part.get_content_subtype() == 'html'
             else apprise.NotifyFormat.TEXT)
    else:
        body = ''
        body_format = apprise.NotifyFormat.TEXT
    attachments = [_parseattachment(part) for part in msg.iter_attachments()
                   if isinstance(part, EmailMessage)]
    return EmailNotification(
        title=title,
        body=body,
        body_format=body_format,
        attachments=attachments
    )


def _parseattachment(part: EmailMessage) -> Attachment:
    return Attachment(data=part.get_content(), filename=part.get_filename(''))


class AttachMailrise(AttachBase):
    """An Apprise attachment type that wraps `Attachment`.

    Data is stored in temporary files for upload.

    Args:
        config: The Mailrise configuration to use.
        attach: The `Attachment` instance.
    """
    detected_name: typ.Optional[str]
    download_path: typ.Optional[str]

    location = ContentLocation.LOCAL

    _mrfile = None  # Satisfy mypy by initializing as an Optional.

    def __init__(self, config: MailriseConfig, attach: Attachment, **kwargs) -> None:
        super().__init__(**kwargs)
        self._mrconfig = config
        self._mrattach = attach

    def download(self) -> bool:
        self.invalidate()

        tfile = NamedTemporaryFile(delete=False)
        tfile.write(self._mrattach.data)
        tfile.close()
        self._mrfile = tfile
        self.download_path = tfile.name
        self.detected_name = self._mrattach.filename

        return True  # Indicates the "download" was successful.

    def invalidate(self) -> None:
        tfile = self._mrfile
        if tfile:
            try:
                os.remove(tfile.name)
            except (FileNotFoundError, OSError):
                self._mrconfig.logger.info(
                    'Failed to delete attachment file: %s', tfile.name)
            self._mrfile = None
        super().invalidate()

    def url(self, **kwargs) -> str:
        return f'mailrise://{hex(id(self))}'

    @staticmethod
    def parse_url(url: str, **kwargs):
        return None
