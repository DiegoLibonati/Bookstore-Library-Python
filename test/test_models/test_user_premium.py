import pytest

from bookstore.models.book_model import BookModel
from bookstore.models.user_premium_model import UserPremiumModel
from bookstore.utils.exceptions import BusinessError, NotFoundError


class TestUserPremiumInit:
    def test_id_is_string(self, user_premium: UserPremiumModel) -> None:
        assert isinstance(user_premium.id, str)

    def test_id_is_non_empty(self, user_premium: UserPremiumModel) -> None:
        assert len(user_premium.id) > 0

    def test_complete_name(self, user_premium: UserPremiumModel) -> None:
        assert user_premium.complete_name == "Carlos Skere"

    def test_address(self, user_premium: UserPremiumModel) -> None:
        assert user_premium.address == "Calle False 1234"

    def test_rented_books_initially_empty(self, user_premium: UserPremiumModel) -> None:
        assert user_premium.rented_books == []

    def test_each_instance_has_unique_id(self) -> None:
        u1 = UserPremiumModel(name="A", surname="B", address="C")
        u2 = UserPremiumModel(name="A", surname="B", address="C")
        assert u1.id != u2.id


class TestUserPremiumRentBook:
    def test_rent_book_adds_to_rented_books(self, user_premium: UserPremiumModel, book: BookModel) -> None:
        user_premium.rent_book(book=book)
        assert book in user_premium.rented_books

    def test_rent_book_decreases_book_units(self, user_premium: UserPremiumModel, book: BookModel) -> None:
        initial_units = book.units
        user_premium.rent_book(book=book)
        assert book.units == initial_units - 1

    def test_rent_multiple_books(self, user_premium: UserPremiumModel, book: BookModel, book_secondary: BookModel) -> None:
        user_premium.rent_book(book=book)
        user_premium.rent_book(book=book_secondary)
        assert len(user_premium.rented_books) == 2

    def test_rent_book_raises_business_error_when_same_book_already_rented(self, user_premium: UserPremiumModel, book: BookModel) -> None:
        user_premium.rent_book(book=book)
        with pytest.raises(BusinessError):
            user_premium.rent_book(book=book)

    def test_rent_book_raises_business_error_when_out_of_stock(self, user_premium: UserPremiumModel, book_no_stock: BookModel) -> None:
        with pytest.raises(BusinessError):
            user_premium.rent_book(book=book_no_stock)


class TestUserPremiumReturnBook:
    def test_return_book_removes_from_rented_books(self, user_premium: UserPremiumModel, book: BookModel) -> None:
        user_premium.rent_book(book=book)
        user_premium.return_book(book=book)
        assert book not in user_premium.rented_books

    def test_return_book_increases_book_units(self, user_premium: UserPremiumModel, book: BookModel) -> None:
        initial_units = book.units
        user_premium.rent_book(book=book)
        user_premium.return_book(book=book)
        assert book.units == initial_units

    def test_return_book_raises_not_found_error_when_book_not_rented(self, user_premium: UserPremiumModel, book: BookModel) -> None:
        with pytest.raises(NotFoundError):
            user_premium.return_book(book=book)

    def test_return_specific_book_from_multiple_rented(self, user_premium: UserPremiumModel, book: BookModel, book_secondary: BookModel) -> None:
        user_premium.rent_book(book=book)
        user_premium.rent_book(book=book_secondary)
        user_premium.return_book(book=book)
        assert book not in user_premium.rented_books
        assert book_secondary in user_premium.rented_books


class TestUserPremiumStr:
    def test_str_returns_string(self, user_premium: UserPremiumModel) -> None:
        assert isinstance(str(user_premium), str)

    def test_str_contains_id(self, user_premium: UserPremiumModel) -> None:
        assert user_premium.id in str(user_premium)

    def test_str_contains_complete_name(self, user_premium: UserPremiumModel) -> None:
        assert user_premium.complete_name in str(user_premium)

    def test_str_contains_rented_book_name_when_renting(self, user_premium: UserPremiumModel, book: BookModel) -> None:
        user_premium.rent_book(book=book)
        assert book.name in str(user_premium)
