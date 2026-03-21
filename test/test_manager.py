import pytest

from bookstore.manager import Manager
from bookstore.models.book_model import BookModel
from bookstore.models.user_normal_model import UserNormalModel
from bookstore.models.user_premium_model import UserPremiumModel
from bookstore.utils.exceptions import ConflictError, NotFoundError, ValidationError


class TestManagerInit:
    def test_name(self, manager: Manager) -> None:
        assert manager.name == "Libreria Test"

    def test_books_initially_empty(self, manager: Manager) -> None:
        assert manager.books == {}

    def test_users_initially_empty(self, manager: Manager) -> None:
        assert manager.users == {}

    def test_books_values_initially_empty(self, manager: Manager) -> None:
        assert list(manager.books_values) == []

    def test_users_values_initially_empty(self, manager: Manager) -> None:
        assert list(manager.users_values) == []


class TestManagerRegisterUser:
    def test_register_user_normal(self, manager: Manager, user_normal: UserNormalModel) -> None:
        manager.register_user(user=user_normal)
        assert user_normal in manager.users_values

    def test_register_user_premium(self, manager: Manager, user_premium: UserPremiumModel) -> None:
        manager.register_user(user=user_premium)
        assert user_premium in manager.users_values

    def test_register_user_stores_by_id(self, manager: Manager, user_normal: UserNormalModel) -> None:
        manager.register_user(user=user_normal)
        assert manager.users[user_normal.id] is user_normal

    def test_register_user_none_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.register_user(user=None)

    def test_register_user_invalid_type_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.register_user(user="invalid")

    def test_register_user_already_exists_raises_conflict_error(self, manager: Manager, user_normal: UserNormalModel) -> None:
        manager.register_user(user=user_normal)
        with pytest.raises(ConflictError):
            manager.register_user(user=user_normal)


class TestManagerRemoveUser:
    def test_remove_user_normal(self, manager: Manager, user_normal: UserNormalModel) -> None:
        manager.register_user(user=user_normal)
        manager.remove_user(user=user_normal)
        assert user_normal not in manager.users_values

    def test_remove_user_premium(self, manager: Manager, user_premium: UserPremiumModel) -> None:
        manager.register_user(user=user_premium)
        manager.remove_user(user=user_premium)
        assert user_premium not in manager.users_values

    def test_remove_user_none_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.remove_user(user=None)

    def test_remove_user_invalid_type_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.remove_user(user="invalid")

    def test_remove_user_not_registered_raises_not_found_error(self, manager: Manager, user_normal: UserNormalModel) -> None:
        with pytest.raises(NotFoundError):
            manager.remove_user(user=user_normal)


class TestManagerAddBook:
    def test_add_book(self, manager: Manager, book: BookModel) -> None:
        manager.add_book(book=book)
        assert book in manager.books_values

    def test_add_book_stores_by_id(self, manager: Manager, book: BookModel) -> None:
        manager.add_book(book=book)
        assert manager.books[book.id] is book

    def test_add_book_none_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.add_book(book=None)

    def test_add_book_invalid_type_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.add_book(book="invalid")


class TestManagerRemoveBook:
    def test_remove_book(self, manager: Manager, book: BookModel) -> None:
        manager.add_book(book=book)
        manager.remove_book(book=book)
        assert book not in manager.books_values

    def test_remove_book_none_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.remove_book(book=None)

    def test_remove_book_invalid_type_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.remove_book(book="invalid")

    def test_remove_book_not_in_library_raises_not_found_error(self, manager: Manager, book: BookModel) -> None:
        with pytest.raises(NotFoundError):
            manager.remove_book(book=book)


class TestManagerRentBook:
    def test_rent_book_for_user_normal(self, manager: Manager, user_normal: UserNormalModel, book: BookModel) -> None:
        manager.register_user(user=user_normal)
        manager.add_book(book=book)
        manager.rent_book(user=user_normal, book=book)
        assert user_normal.rented_book is book

    def test_rent_book_for_user_premium(self, manager: Manager, user_premium: UserPremiumModel, book: BookModel) -> None:
        manager.register_user(user=user_premium)
        manager.add_book(book=book)
        manager.rent_book(user=user_premium, book=book)
        assert book in user_premium.rented_books

    def test_rent_book_invalid_user_raises_validation_error(self, manager: Manager, book: BookModel) -> None:
        with pytest.raises(ValidationError):
            manager.rent_book(user=None, book=book)

    def test_rent_book_invalid_user_type_raises_validation_error(self, manager: Manager, book: BookModel) -> None:
        with pytest.raises(ValidationError):
            manager.rent_book(user="invalid", book=book)

    def test_rent_book_invalid_book_raises_validation_error(self, manager: Manager, user_normal: UserNormalModel) -> None:
        with pytest.raises(ValidationError):
            manager.rent_book(user=user_normal, book=None)

    def test_rent_book_invalid_book_type_raises_validation_error(self, manager: Manager, user_normal: UserNormalModel) -> None:
        with pytest.raises(ValidationError):
            manager.rent_book(user=user_normal, book="invalid")


class TestManagerReturnBook:
    def test_return_book_for_user_normal(self, manager: Manager, user_normal: UserNormalModel, book: BookModel) -> None:
        manager.register_user(user=user_normal)
        manager.add_book(book=book)
        manager.rent_book(user=user_normal, book=book)
        manager.return_book(user=user_normal)
        assert user_normal.rented_book is None

    def test_return_book_for_user_premium(self, manager: Manager, user_premium: UserPremiumModel, book: BookModel) -> None:
        manager.register_user(user=user_premium)
        manager.add_book(book=book)
        manager.rent_book(user=user_premium, book=book)
        manager.return_book(user=user_premium, book=book)
        assert book not in user_premium.rented_books

    def test_return_book_invalid_user_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.return_book(user=None)

    def test_return_book_invalid_user_type_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.return_book(user="invalid")

    def test_return_book_invalid_book_type_raises_validation_error(self, manager: Manager, user_normal: UserNormalModel) -> None:
        with pytest.raises(ValidationError):
            manager.return_book(user=user_normal, book="invalid")


class TestManagerStr:
    def test_str_returns_string(self, manager: Manager) -> None:
        assert isinstance(str(manager), str)

    def test_str_contains_name(self, manager: Manager) -> None:
        assert manager.name in str(manager)
