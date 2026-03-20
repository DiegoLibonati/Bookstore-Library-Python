from uuid import uuid4

from bookstore.configs.logger_config import setup_logger

logger = setup_logger("Bookstore - book.py")


class Book:
    def __init__(self, name: str, description: str, author: str, units: int, banner_url: str = "") -> None:
        self.__id = str(uuid4())
        self.__name = name
        self.__description = description
        self.__author = author
        self.__units = units
        self.__banner_url = banner_url

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def author(self) -> str:
        return self.__author

    @property
    def units(self) -> int:
        return self.__units

    @property
    def banner_url(self) -> str:
        return self.__banner_url

    @property
    def stock(self) -> bool:
        return bool(self.units)

    @banner_url.setter
    def banner_url(self, value: str) -> None:
        self.__banner_url = value

    def decrease_unit(self) -> None:
        if not self.stock:
            return

        new_units = self.units - 1

        if new_units <= 0:
            self.__units = 0
            return

        self.__units = new_units

    def increase_unit(self) -> None:
        self.__units += 1

    def __str__(self) -> str:
        return (
            f"----- Book {self.id} -----\n"
            f"Book ID: {self.id}\n"
            f"Book Name: {self.name}\n"
            f"Book Description: {self.description}\n"
            f"Book Author: {self.author}\n"
            f"Book Units: {self.units}\n"
            f"Book Banner: {self.banner_url}\n\n"
        )


def main() -> None:
    book = Book(
        name="Drácula",
        description="Es una novela de fantasía gótica escrita por Bram Stoker, publicada en 1897.",
        author="Bram Stoker",
        units=20,
    )

    logger.info(book)


if __name__ == "__main__":
    main()
