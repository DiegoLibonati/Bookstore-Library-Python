import pytest

from lend_book.models.book_model import BookModel
from lend_book.models.user_normal_model import UserNormalModel
from lend_book.utils.exceptions import BusinessError, NotFoundError


class TestUserNormalModelInit:
    @pytest.mark.unit
    def test_id_is_string(self) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        assert isinstance(user.id, str)

    @pytest.mark.unit
    def test_id_is_not_empty(self) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        assert len(user.id) > 0

    @pytest.mark.unit
    def test_complete_name(self) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        assert user.complete_name == "Pepe García"

    @pytest.mark.unit
    def test_address_property(self) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle False 123")
        assert user.address == "Calle False 123"

    @pytest.mark.unit
    def test_rented_book_initial_is_none(self) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        assert user.rented_book is None

    @pytest.mark.unit
    def test_two_users_have_different_ids(self) -> None:
        user_a: UserNormalModel = UserNormalModel(name="A", surname="A", address="Calle 1")
        user_b: UserNormalModel = UserNormalModel(name="B", surname="B", address="Calle 2")
        assert user_a.id != user_b.id


class TestUserNormalModelRentBook:
    @pytest.mark.unit
    def test_rent_book_assigns_rented_book(self, book_with_units: BookModel) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        user.rent_book(book=book_with_units)
        assert user.rented_book is book_with_units

    @pytest.mark.unit
    def test_rent_book_decreases_book_units(self, book_with_units: BookModel) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        initial_units: int = book_with_units.units
        user.rent_book(book=book_with_units)
        assert book_with_units.units == initial_units - 1

    @pytest.mark.unit
    def test_rent_book_raises_business_error_when_already_renting(self, book_with_units: BookModel) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        other_book: BookModel = BookModel(name="Other", description="Desc", author="Author", units=3)
        user.rent_book(book=book_with_units)
        with pytest.raises(BusinessError):
            user.rent_book(book=other_book)

    @pytest.mark.unit
    def test_rent_book_raises_business_error_when_out_of_stock(self, book_out_of_stock: BookModel) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        with pytest.raises(BusinessError):
            user.rent_book(book=book_out_of_stock)

    @pytest.mark.unit
    def test_rent_book_error_when_already_renting_has_correct_code(self, book_with_units: BookModel) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        other_book: BookModel = BookModel(name="Other", description="Desc", author="Author", units=3)
        user.rent_book(book=book_with_units)
        with pytest.raises(BusinessError) as exc_info:
            user.rent_book(book=other_book)
        assert exc_info.value.code == "ERROR_BOOK_RETURN_REQUIRED"

    @pytest.mark.unit
    def test_rent_book_out_of_stock_error_has_correct_code(self, book_out_of_stock: BookModel) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        with pytest.raises(BusinessError) as exc_info:
            user.rent_book(book=book_out_of_stock)
        assert exc_info.value.code == "ERROR_OUT_OF_STOCK"


class TestUserNormalModelReturnBook:
    @pytest.mark.unit
    def test_return_book_clears_rented_book(self, book_with_units: BookModel) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        user.rent_book(book=book_with_units)
        user.return_book()
        assert user.rented_book is None

    @pytest.mark.unit
    def test_return_book_increases_book_units(self, book_with_units: BookModel) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        initial_units: int = book_with_units.units
        user.rent_book(book=book_with_units)
        user.return_book()
        assert book_with_units.units == initial_units

    @pytest.mark.unit
    def test_return_book_raises_not_found_when_no_book_rented(self) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        with pytest.raises(NotFoundError):
            user.return_book()

    @pytest.mark.unit
    def test_return_book_allows_renting_again(self, book_with_units: BookModel) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        other_book: BookModel = BookModel(name="Other", description="Desc", author="Author", units=3)
        user.rent_book(book=book_with_units)
        user.return_book()
        user.rent_book(book=other_book)
        assert user.rented_book is other_book

    @pytest.mark.unit
    def test_return_book_not_found_error_has_correct_code(self) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        with pytest.raises(NotFoundError) as exc_info:
            user.return_book()
        assert exc_info.value.code == "NOT_FOUND_RENTED_BOOK"


class TestUserNormalModelStr:
    @pytest.mark.unit
    def test_str_contains_user_id(self) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        assert user.id in str(user)

    @pytest.mark.unit
    def test_str_contains_complete_name(self) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        assert "Pepe García" in str(user)

    @pytest.mark.unit
    def test_str_shows_none_when_no_book_rented(self) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        assert "None" in str(user)

    @pytest.mark.unit
    def test_str_shows_book_name_when_rented(self, book_with_units: BookModel) -> None:
        user: UserNormalModel = UserNormalModel(name="Pepe", surname="García", address="Calle 1")
        user.rent_book(book=book_with_units)
        assert book_with_units.name in str(user)
