from enum import StrEnum

from decorator import NotificationWithAttachment
from notification_service import SmsNotificationService, EmailNotificationService
from utils import ExternalSmsNotificationService


class NotificationType(StrEnum):
    EMAIL = 'email'
    SMS = 'sms'


class NotificationFactory:
    @staticmethod
    def create_notification_service(notification_type: NotificationType, attachment: bool = False):
        if notification_type == NotificationType.EMAIL:
            notification_service = EmailNotificationService()
        elif notification_type == NotificationType.SMS:
            notification_service = SmsNotificationService(ExternalSmsNotificationService())
        else:
            raise ValueError(f'Unknown notification type: {notification_type}')

        if attachment:
            notification_service = NotificationWithAttachment(notification_service)
        return notification_service
