from notification import AttachmentNotification
from notification_service import AbstractNotificationService


class NotificationWithAttachment:
    def __init__(self, notification_service: AbstractNotificationService):
        self.notification_service = notification_service

    def save_attachment(self, attachment: str):
        print(f"Saving attachment {attachment} to disk")
        return 'link_to_attachment'

    def send(self, notification: AttachmentNotification):
        link = self.save_attachment(notification.attachment)
        message_with_attachment = f"{notification.message} with attachment {link}"
        notification.message = message_with_attachment
        self.notification_service.send(notification)
