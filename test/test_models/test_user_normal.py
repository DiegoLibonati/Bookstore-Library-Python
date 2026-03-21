import pytest

from bookstore.models.book_model import BookModel
from bookstore.models.user_normal_model import UserNormalModel
from bookstore.utils.exceptions import BusinessError, NotFoundError


class TestUserNormalInit:
    def test_id_is_string(self, user_normal: UserNormalModel) -> None:
        assert isinstance(user_normal.id, str)

    def test_id_is_non_empty(self, user_normal: UserNormalModel) -> None:
        assert len(user_normal.id) > 0

    def test_complete_name(self, user_normal: UserNormalModel) -> None:
        assert user_normal.complete_name == "Pepe Alcachofaz"

    def test_address(self, user_normal: UserNormalModel) -> None:
        assert user_normal.address == "Calle False 123"

    def test_rented_book_initially_none(self, user_normal: UserNormalModel) -> None:
        assert user_normal.rented_book is None

    def test_each_instance_has_unique_id(self) -> None:
        u1 = UserNormalModel(name="A", surname="B", address="C")
        u2 = UserNormalModel(name="A", surname="B", address="C")
        assert u1.id != u2.id


class TestUserNormalRentBook:
    def test_rent_book_sets_rented_book(self, user_normal: UserNormalModel, book: BookModel) -> None:
        user_normal.rent_book(book=book)
        assert user_normal.rented_book is book

    def test_rent_book_decreases_book_units(self, user_normal: UserNormalModel, book: BookModel) -> None:
        initial_units = book.units
        user_normal.rent_book(book=book)
        assert book.units == initial_units - 1

    def test_rent_book_raises_business_error_when_already_renting(self, user_normal: UserNormalModel, book: BookModel, book_secondary: BookModel) -> None:
        user_normal.rent_book(book=book)
        with pytest.raises(BusinessError):
            user_normal.rent_book(book=book_secondary)

    def test_rent_book_raises_business_error_when_out_of_stock(self, user_normal: UserNormalModel, book_no_stock: BookModel) -> None:
        with pytest.raises(BusinessError):
            user_normal.rent_book(book=book_no_stock)


class TestUserNormalReturnBook:
    def test_return_book_clears_rented_book(self, user_normal: UserNormalModel, book: BookModel) -> None:
        user_normal.rent_book(book=book)
        user_normal.return_book()
        assert user_normal.rented_book is None

    def test_return_book_increases_book_units(self, user_normal: UserNormalModel, book: BookModel) -> None:
        initial_units = book.units
        user_normal.rent_book(book=book)
        user_normal.return_book()
        assert book.units == initial_units

    def test_return_book_raises_not_found_error_when_nothing_rented(self, user_normal: UserNormalModel) -> None:
        with pytest.raises(NotFoundError):
            user_normal.return_book()


class TestUserNormalStr:
    def test_str_returns_string(self, user_normal: UserNormalModel) -> None:
        assert isinstance(str(user_normal), str)

    def test_str_contains_id(self, user_normal: UserNormalModel) -> None:
        assert user_normal.id in str(user_normal)

    def test_str_contains_complete_name(self, user_normal: UserNormalModel) -> None:
        assert user_normal.complete_name in str(user_normal)

    def test_str_contains_rented_book_name_when_renting(self, user_normal: UserNormalModel, book: BookModel) -> None:
        user_normal.rent_book(book=book)
        assert book.name in str(user_normal)
