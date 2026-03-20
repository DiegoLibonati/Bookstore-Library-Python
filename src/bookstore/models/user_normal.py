from bookstore.configs.logger_config import setup_logger
from bookstore.constants.codes import CODE_ERROR_BOOK_RETURN_REQUIRED, CODE_ERROR_OUT_OF_STOCK, CODE_NOT_FOUND_RENTED_BOOK
from bookstore.constants.messages import MESSAGE_ERROR_BOOK_RETURN_REQUIRED, MESSAGE_ERROR_OUT_OF_STOCK, MESSAGE_NOT_FOUND_RENTED_BOOK
from bookstore.models.book import Book
from bookstore.models.user import User
from bookstore.utils.exceptions import BusinessError, NotFoundError

logger = setup_logger("Bookstore - user_normal.py")


class UserNormal(User):
    def __init__(self, name: str, surname: str, address: str) -> None:
        super().__init__(name=name, surname=surname, address=address)
        self.__rented_book: Book = None

    @property
    def rented_book(self) -> Book:
        return self.__rented_book

    def rent_book(self, book: Book) -> None:
        if self.rented_book:
            raise BusinessError(code=CODE_ERROR_BOOK_RETURN_REQUIRED, message=MESSAGE_ERROR_BOOK_RETURN_REQUIRED.format(name=self.rented_book.name))

        if not book.stock:
            raise BusinessError(code=CODE_ERROR_OUT_OF_STOCK, message=MESSAGE_ERROR_OUT_OF_STOCK.format(name=book.name))

        book.decrease_unit()
        self.__rented_book = book

    def return_book(self) -> None:
        if not self.rented_book:
            raise NotFoundError(code=CODE_NOT_FOUND_RENTED_BOOK, message=MESSAGE_NOT_FOUND_RENTED_BOOK)

        self.rented_book.increase_unit()
        self.__rented_book = None

    def __str__(self) -> None:
        return (
            f"----- User Normal {self.id} -----\n"
            f"User ID: {self.id}\n"
            f"User: {self.complete_name}\n"
            f"User Adress: {self.address}\n"
            f"Book Rented: {self.rented_book.name if self.rented_book else None}\n\n"
        )


def main() -> None:
    dracula_book = Book(
        name="Drácula",
        description="Es una novela de fantasía gótica escrita por Bram Stoker, publicada en 1897.",
        author="Bram Stoker",
        units=20,
    )
    la_clase_de_griego_book = Book(
        name="LA CLASE DE GRIEGO",
        description="En Seúl, una mujer asiste a clases de griego antiguo.",
        author="KANG, HAN",
        units=1,
    )
    gravity_falls_book = Book(
        name="Gravity Falls",
        description="Este libro está lleno de datos y confesiones escalofriantes para satisfacer tu curiosidad.",
        author="Alex Hirsch",
        units=5,
    )

    user_normal = UserNormal(name="Pepe", surname="Alcachofaz", address="Calle False 123")
    user_normal_2 = UserNormal(name="Sergio", surname="Sorg", address="Calle False 12345")

    user_normal.rent_book(book=dracula_book)

    logger.info(user_normal)
    logger.info(user_normal_2)

    logger.info(dracula_book)
    logger.info(la_clase_de_griego_book)
    logger.info(gravity_falls_book)


if __name__ == "__main__":
    main()
