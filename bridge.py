from adapter import AbstractNotificationAdapter


class UserNotification:
    def __init__(self, notification_adapter: AbstractNotificationAdapter):
        self.notification_adapter = notification_adapter

    def send(self):
        self.notification_adapter.send_notification()
