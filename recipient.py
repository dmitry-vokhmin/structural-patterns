from abc import ABC, abstractmethod


class AbstractRecipient(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class Recipient(AbstractRecipient):
    def __init__(self, name: str):
        self.name = name

    def send(self, message: str):
        print(f'{self.name} received message: \n {message}')


class GroupRecipient(AbstractRecipient):
    def __init__(self, group_name: str, recipients: list[AbstractRecipient]):
        self.group_name = group_name
        self.recipients = recipients

    def send(self, message: str):
        print(f'{self.group_name} received message: {message}')
        for recipient in self.recipients:
            recipient.send(message)
