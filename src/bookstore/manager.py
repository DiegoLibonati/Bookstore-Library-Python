from collections.abc import ValuesView

from bookstore.configs.logger_config import setup_logger
from bookstore.constants.codes import CODE_ALREADY_EXISTS_USER, CODE_NOT_FOUND_BOOK, CODE_NOT_FOUND_USER, CODE_NOT_VALID_BOOK, CODE_NOT_VALID_USER
from bookstore.constants.messages import (
    MESSAGE_ALREADY_EXISTS_USER,
    MESSAGE_NOT_FOUND_BOOK,
    MESSAGE_NOT_FOUND_USER,
    MESSAGE_NOT_VALID_BOOK,
    MESSAGE_NOT_VALID_USER,
)
from bookstore.models.book_model import BookModel
from bookstore.models.user_normal_model import UserNormalModel
from bookstore.models.user_premium_model import UserPremiumModel
from bookstore.utils.exceptions import ConflictError, NotFoundError, ValidationError

logger = setup_logger("Bookstore - manager.py")


class Manager:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__books: dict[str, BookModel] = {}
        self.__users: dict[str, UserNormalModel | UserPremiumModel] = {}

    @property
    def name(self) -> str:
        return self.__name

    @property
    def books(self) -> dict[str, BookModel]:
        return self.__books

    @property
    def users(self) -> dict[str, UserNormalModel | UserPremiumModel]:
        return self.__users

    @property
    def books_values(self) -> ValuesView[BookModel]:
        return self.__books.values()

    @property
    def users_values(self) -> ValuesView[UserNormalModel | UserPremiumModel]:
        return self.__users.values()

    def register_user(self, user: UserNormalModel | UserPremiumModel) -> None:
        if not user or not isinstance(user, UserNormalModel | UserPremiumModel):
            raise ValidationError(code=CODE_NOT_VALID_USER, message=MESSAGE_NOT_VALID_USER)
        if user in self.users_values:
            raise ConflictError(code=CODE_ALREADY_EXISTS_USER, message=MESSAGE_ALREADY_EXISTS_USER)
        self.__users[user.id] = user

    def remove_user(self, user: UserNormalModel | UserPremiumModel) -> None:
        if not user or not isinstance(user, UserNormalModel | UserPremiumModel):
            raise ValidationError(code=CODE_NOT_VALID_USER, message=MESSAGE_NOT_VALID_USER)
        if user not in self.users_values:
            raise NotFoundError(code=CODE_NOT_FOUND_USER, message=MESSAGE_NOT_FOUND_USER)

        del self.__users[user.id]

    def add_book(self, book: BookModel) -> None:
        if not book or not isinstance(book, BookModel):
            raise ValidationError(code=CODE_NOT_VALID_BOOK, message=MESSAGE_NOT_VALID_BOOK)
        self.__books[book.id] = book

    def remove_book(self, book: BookModel) -> None:
        if not book or not isinstance(book, BookModel):
            raise ValidationError(code=CODE_NOT_VALID_BOOK, message=MESSAGE_NOT_VALID_BOOK)
        if book not in self.books_values:
            raise NotFoundError(code=CODE_NOT_FOUND_BOOK, message=MESSAGE_NOT_FOUND_BOOK.format(name=book.name))

        del self.__books[book.id]

    def rent_book(self, user: UserNormalModel | UserPremiumModel, book: BookModel) -> None:
        if not user or not isinstance(user, UserNormalModel | UserPremiumModel):
            raise ValidationError(code=CODE_NOT_VALID_USER, message=MESSAGE_NOT_VALID_USER)
        if not book or not isinstance(book, BookModel):
            raise ValidationError(code=CODE_NOT_VALID_BOOK, message=MESSAGE_NOT_VALID_BOOK)

        user.rent_book(book=book)

    def return_book(self, user: UserNormalModel | UserPremiumModel, book: BookModel = None) -> None:
        if not user or not isinstance(user, UserNormalModel | UserPremiumModel):
            raise ValidationError(code=CODE_NOT_VALID_USER, message=MESSAGE_NOT_VALID_USER)
        if book and not isinstance(book, BookModel):
            raise ValidationError(code=CODE_NOT_VALID_BOOK, message=MESSAGE_NOT_VALID_BOOK)

        if isinstance(user, UserPremiumModel):
            user.return_book(book=book)
            return

        user.return_book()

    def str_users(self) -> None:
        logger.info(f"----- Library Users {self.name} -----")
        for user in self.users_values:
            logger.info(user)

    def str_books(self) -> None:
        logger.info(f"----- Library Books {self.name} -----")
        for book in self.books_values:
            logger.info(book)

    def __str__(self) -> str:
        return f"----- Library {self.name} -----\nLibrary Name: {self.name}\nLibrary Users: {self.users_values}\nLibrary Books: {self.books_values}\n\n"


def main() -> None:
    # Library
    library = Manager(name="Libreria LaRosca")

    # Books
    dracula_book = BookModel(
        name="Drácula",
        description="Es una novela de fantasía gótica escrita por Bram Stoker, publicada en 1897.",
        author="Bram Stoker",
        units=20,
    )
    la_clase_de_griego_book = BookModel(
        name="LA CLASE DE GRIEGO",
        description="En Seúl, una mujer asiste a clases de griego antiguo.",
        author="KANG, HAN",
        units=1,
    )
    gravity_falls_book = BookModel(
        name="Gravity Falls",
        description="Este libro está lleno de datos y confesiones escalofriantes para satisfacer tu curiosidad.",
        author="Alex Hirsch",
        units=5,
    )

    # Users
    user_normal = UserNormalModel(name="Pepe", surname="Alcachofaz", address="Calle False 123")
    user_normal_2 = UserNormalModel(name="Sergio", surname="Sorg", address="Calle False 12345")
    user_premium = UserPremiumModel(name="Carlos", surname="Skere", address="Calle False 1234")

    library.register_user(user=user_normal)
    library.register_user(user=user_normal_2)
    library.register_user(user=user_premium)

    library.add_book(dracula_book)
    library.add_book(la_clase_de_griego_book)
    library.add_book(gravity_falls_book)

    library.rent_book(user=user_normal, book=dracula_book)
    library.rent_book(user=user_premium, book=dracula_book)
    library.rent_book(user=user_premium, book=la_clase_de_griego_book)
    library.rent_book(user=user_premium, book=gravity_falls_book)

    library.return_book(user=user_normal)
    library.return_book(user=user_premium, book=dracula_book)

    logger.info(library)
    library.str_users()
    library.str_books()


if __name__ == "__main__":
    main()
