from abc import ABC, abstractmethod

from notification import Notification
from utils import ExternalSmsNotificationService


class AbstractNotificationService(ABC):
    @abstractmethod
    def send(self, notification: Notification):
        pass


class EmailNotificationService(AbstractNotificationService):

    def send(self, notification: Notification):
        emails = []
        for user in notification.users:
            emails.extend(user.get_email())
        print(f"Sending email to {emails} with message: {notification.message}")


class SmsNotificationService(AbstractNotificationService):
    def __init__(self, sms_service: ExternalSmsNotificationService):
        self.sms_service = sms_service

    def send(self, notification: Notification):
        phones = []
        for user in notification.users:
            phones.extend(user.get_phone())

        for phone in phones:
            self.sms_service.send_sms(phone, notification.message)
