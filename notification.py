from recipient import AbstractRecipient


class Notification:
    def __init__(self, message: str, recipient: list[AbstractRecipient]):
        self.recipient = recipient
        self.message = message

    def send(self):
        for recipient in self.recipient:
            recipient.send(self.message)


class NotificationWithSubject(Notification):
    def __init__(self, notification: Notification, subject: str):
        super().__init__(notification.message, notification.recipient)
        self.message = f'Subject: {subject} \n {notification.message}'
        self.subject = subject


class NotificationWithAttachment(Notification):
    def __init__(self, notification: Notification, attachment: str):
        super().__init__(notification.message, notification.recipient)
        self.message = f'{notification.message} \n Attachment: {attachment}'
        self.attachment = attachment
