import pytest

from lend_book.models.book_model import BookModel
from lend_book.models.user_premium_model import UserPremiumModel
from lend_book.utils.exceptions import BusinessError, NotFoundError


class TestUserPremiumModelInit:
    @pytest.mark.unit
    def test_id_is_string(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        assert isinstance(user.id, str)

    @pytest.mark.unit
    def test_id_is_not_empty(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        assert len(user.id) > 0

    @pytest.mark.unit
    def test_complete_name(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        assert user.complete_name == "Carlos Skere"

    @pytest.mark.unit
    def test_address_property(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle False 1234")
        assert user.address == "Calle False 1234"

    @pytest.mark.unit
    def test_rented_books_initial_is_empty_list(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        assert user.rented_books == []

    @pytest.mark.unit
    def test_two_users_have_different_ids(self) -> None:
        user_a: UserPremiumModel = UserPremiumModel(name="A", surname="A", address="Calle 1")
        user_b: UserPremiumModel = UserPremiumModel(name="B", surname="B", address="Calle 2")
        assert user_a.id != user_b.id


class TestUserPremiumModelRentBook:
    @pytest.mark.unit
    def test_rent_book_adds_to_rented_books(self, book_with_units: BookModel) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        user.rent_book(book=book_with_units)
        assert book_with_units in user.rented_books

    @pytest.mark.unit
    def test_rent_book_decreases_units(self, book_with_units: BookModel) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        initial_units: int = book_with_units.units
        user.rent_book(book=book_with_units)
        assert book_with_units.units == initial_units - 1

    @pytest.mark.unit
    def test_rent_multiple_books(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        book_a: BookModel = BookModel(name="Book A", description="Desc", author="Author", units=2)
        book_b: BookModel = BookModel(name="Book B", description="Desc", author="Author", units=2)
        book_c: BookModel = BookModel(name="Book C", description="Desc", author="Author", units=2)
        user.rent_book(book=book_a)
        user.rent_book(book=book_b)
        user.rent_book(book=book_c)
        assert len(user.rented_books) == 3

    @pytest.mark.unit
    def test_rent_book_raises_business_error_when_same_book_rented_twice(self, book_with_units: BookModel) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        user.rent_book(book=book_with_units)
        with pytest.raises(BusinessError):
            user.rent_book(book=book_with_units)

    @pytest.mark.unit
    def test_rent_book_raises_business_error_when_out_of_stock(self, book_out_of_stock: BookModel) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        with pytest.raises(BusinessError):
            user.rent_book(book=book_out_of_stock)

    @pytest.mark.unit
    def test_rent_same_book_error_has_correct_code(self, book_with_units: BookModel) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        user.rent_book(book=book_with_units)
        with pytest.raises(BusinessError) as exc_info:
            user.rent_book(book=book_with_units)
        assert exc_info.value.code == "ALREADY_EXISTS_BOOK_RENTED"

    @pytest.mark.unit
    def test_rent_out_of_stock_error_has_correct_code(self, book_out_of_stock: BookModel) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        with pytest.raises(BusinessError) as exc_info:
            user.rent_book(book=book_out_of_stock)
        assert exc_info.value.code == "ERROR_OUT_OF_STOCK"


class TestUserPremiumModelReturnBook:
    @pytest.mark.unit
    def test_return_book_removes_from_rented_books(self, book_with_units: BookModel) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        user.rent_book(book=book_with_units)
        user.return_book(book=book_with_units)
        assert book_with_units not in user.rented_books

    @pytest.mark.unit
    def test_return_book_increases_units(self, book_with_units: BookModel) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        initial_units: int = book_with_units.units
        user.rent_book(book=book_with_units)
        user.return_book(book=book_with_units)
        assert book_with_units.units == initial_units

    @pytest.mark.unit
    def test_return_one_book_keeps_others(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        book_a: BookModel = BookModel(name="Book A", description="Desc", author="Author", units=2)
        book_b: BookModel = BookModel(name="Book B", description="Desc", author="Author", units=2)
        user.rent_book(book=book_a)
        user.rent_book(book=book_b)
        user.return_book(book=book_a)
        assert book_b in user.rented_books
        assert book_a not in user.rented_books

    @pytest.mark.unit
    def test_return_book_raises_not_found_when_not_rented(self, book_with_units: BookModel) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        with pytest.raises(NotFoundError):
            user.return_book(book=book_with_units)

    @pytest.mark.unit
    def test_return_book_not_found_error_has_correct_code(self, book_with_units: BookModel) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        with pytest.raises(NotFoundError) as exc_info:
            user.return_book(book=book_with_units)
        assert exc_info.value.code == "NOT_FOUND_RENTED_BOOK"


class TestUserPremiumModelGetListNameRentedBooks:
    @pytest.mark.unit
    def test_returns_empty_list_when_no_books_rented(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        result: list[str] = user._get_list_name_rented_books()
        assert result == []

    @pytest.mark.unit
    def test_returns_list_of_book_names(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        book_a: BookModel = BookModel(name="Drácula", description="Desc", author="Author", units=2)
        book_b: BookModel = BookModel(name="Gravity Falls", description="Desc", author="Author", units=2)
        user.rent_book(book=book_a)
        user.rent_book(book=book_b)
        result: list[str] = user._get_list_name_rented_books()
        assert "Drácula" in result
        assert "Gravity Falls" in result

    @pytest.mark.unit
    def test_returns_list_with_correct_length(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        book_a: BookModel = BookModel(name="Book A", description="Desc", author="Author", units=2)
        book_b: BookModel = BookModel(name="Book B", description="Desc", author="Author", units=2)
        user.rent_book(book=book_a)
        user.rent_book(book=book_b)
        result: list[str] = user._get_list_name_rented_books()
        assert len(result) == 2


class TestUserPremiumModelStr:
    @pytest.mark.unit
    def test_str_contains_user_id(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        assert user.id in str(user)

    @pytest.mark.unit
    def test_str_contains_complete_name(self) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        assert "Carlos Skere" in str(user)

    @pytest.mark.unit
    def test_str_contains_rented_book_name(self, book_with_units: BookModel) -> None:
        user: UserPremiumModel = UserPremiumModel(name="Carlos", surname="Skere", address="Calle 1")
        user.rent_book(book=book_with_units)
        assert book_with_units.name in str(user)
