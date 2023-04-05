from user import AbstractUser


class Notification:
    def __init__(self, message: str, users: list[AbstractUser]):
        self.users = users
        self.message = message


class AttachmentNotification(Notification):
    def __init__(self, message: str, users: list[AbstractUser], attachment: str):
        super().__init__(message, users)
        self.attachment = attachment
