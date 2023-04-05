from notification import Notification


class UserNotification:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def send_notification(self, notification: Notification):
        self.notification_service.send(notification)
