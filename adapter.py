from abc import ABC, abstractmethod

from notification import Notification


class AbstractNotificationAdapter(ABC):
    @abstractmethod
    def send_notification(self):
        pass


class SmartphoneNotificationAdapter(AbstractNotificationAdapter):
    format = "smartphone"

    def __init__(self, notification):
        self.notification = Notification(notification.message, notification.recipient)
        self.notification.message = f"{self.notification.message} \n Format: {self.format}"

    def send_notification(self):
        self.notification.send()


class TabletNotificationAdapter(AbstractNotificationAdapter):
    format = "tablet"

    def __init__(self, notification):
        self.notification = Notification(notification.message, notification.recipient)
        self.notification.message = f"{self.notification.message} \n Format: {self.format}"

    def send_notification(self):
        self.notification.send()


class DesktopNotificationAdapter(AbstractNotificationAdapter):
    format = "desktop"

    def __init__(self, notification):
        self.notification = Notification(notification.message, notification.recipient)
        self.notification.message = f"{self.notification.message} \n Format: {self.format}"

    def send_notification(self):
        self.notification.send()
