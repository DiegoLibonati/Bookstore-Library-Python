from abc import ABC, abstractmethod
from uuid import uuid4


class UserModel(ABC):
    def __init__(self, name: str, surname: str, address: str) -> None:
        self.__id = str(uuid4())
        self.__name = name
        self.__surname = surname
        self.__address = address

    @property
    def id(self) -> str:
        return self.__id

    @property
    def complete_name(self) -> str:
        return self.__name + " " + self.__surname

    @property
    def address(self) -> str:
        return self.__address

    def __str__(self) -> None:
        return f"----- UserModel {self.id} -----\nUser ID: {self.id}\nUser: {self.complete_name}\nUser Adress: {self.address}\n\n"

    @abstractmethod
    def rent_book(self) -> None:
        pass

    @abstractmethod
    def return_book(self) -> None:
        pass
