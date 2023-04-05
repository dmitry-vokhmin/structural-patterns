from abc import ABC, abstractmethod


class AbstractUser(ABC):
    @abstractmethod
    def get_email(self):
        pass

    @abstractmethod
    def get_phone(self):
        pass


class User(AbstractUser):
    def __init__(self, name: str, email: str, phone: str):
        self._phone = phone
        self._email = email
        self.name = name

    def get_email(self):
        return [self._email]

    def get_phone(self):
        return [self._phone]


class UserGroup(AbstractUser):
    def __init__(self, group_name: str, users: list[User]):
        self.group_name = group_name
        self.users = users

    def get_email(self):
        return [user.get_email()[0] for user in self.users]

    def get_phone(self):
        return [user.get_phone()[0] for user in self.users]
