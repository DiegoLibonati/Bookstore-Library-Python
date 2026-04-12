import pytest

from lend_book.manager import Manager
from lend_book.models.book_model import BookModel
from lend_book.models.user_normal_model import UserNormalModel
from lend_book.models.user_premium_model import UserPremiumModel
from lend_book.utils.exceptions import BusinessError, ConflictError, NotFoundError, ValidationError


class TestManagerInit:
    @pytest.mark.unit
    def test_name_property(self) -> None:
        mgr: Manager = Manager(name="Libreria LaRosca")
        assert mgr.name == "Libreria LaRosca"

    @pytest.mark.unit
    def test_books_initial_empty(self) -> None:
        mgr: Manager = Manager(name="Libreria LaRosca")
        assert mgr.books == {}

    @pytest.mark.unit
    def test_users_initial_empty(self) -> None:
        mgr: Manager = Manager(name="Libreria LaRosca")
        assert mgr.users == {}

    @pytest.mark.unit
    def test_books_values_initial_empty(self) -> None:
        mgr: Manager = Manager(name="Libreria LaRosca")
        assert list(mgr.books_values) == []

    @pytest.mark.unit
    def test_users_values_initial_empty(self) -> None:
        mgr: Manager = Manager(name="Libreria LaRosca")
        assert list(mgr.users_values) == []


class TestManagerRegisterUser:
    @pytest.mark.unit
    def test_register_user_normal(self, manager: Manager, user_normal: UserNormalModel) -> None:
        manager.register_user(user=user_normal)
        assert user_normal in manager.users_values

    @pytest.mark.unit
    def test_register_user_premium(self, manager: Manager, user_premium: UserPremiumModel) -> None:
        manager.register_user(user=user_premium)
        assert user_premium in manager.users_values

    @pytest.mark.unit
    def test_register_user_stores_by_id(self, manager: Manager, user_normal: UserNormalModel) -> None:
        manager.register_user(user=user_normal)
        assert manager.users[user_normal.id] is user_normal

    @pytest.mark.unit
    def test_register_user_none_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.register_user(user=None)

    @pytest.mark.unit
    def test_register_user_invalid_type_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.register_user(user="not-a-user")

    @pytest.mark.unit
    def test_register_duplicate_user_raises_conflict_error(self, manager: Manager, user_normal: UserNormalModel) -> None:
        manager.register_user(user=user_normal)
        with pytest.raises(ConflictError):
            manager.register_user(user=user_normal)

    @pytest.mark.unit
    def test_register_validation_error_has_correct_code(self, manager: Manager) -> None:
        with pytest.raises(ValidationError) as exc_info:
            manager.register_user(user=None)
        assert exc_info.value.code == "NOT_VALID_USER"

    @pytest.mark.unit
    def test_register_conflict_error_has_correct_code(self, manager: Manager, user_normal: UserNormalModel) -> None:
        manager.register_user(user=user_normal)
        with pytest.raises(ConflictError) as exc_info:
            manager.register_user(user=user_normal)
        assert exc_info.value.code == "ALREADY_EXISTS_USER"


class TestManagerRemoveUser:
    @pytest.mark.unit
    def test_remove_user_removes_from_dict(self, manager: Manager, user_normal: UserNormalModel) -> None:
        manager.register_user(user=user_normal)
        manager.remove_user(user=user_normal)
        assert user_normal not in manager.users_values

    @pytest.mark.unit
    def test_remove_user_none_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.remove_user(user=None)

    @pytest.mark.unit
    def test_remove_user_invalid_type_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.remove_user(user="not-a-user")

    @pytest.mark.unit
    def test_remove_user_not_registered_raises_not_found_error(self, manager: Manager, user_normal: UserNormalModel) -> None:
        with pytest.raises(NotFoundError):
            manager.remove_user(user=user_normal)

    @pytest.mark.unit
    def test_remove_user_not_found_error_has_correct_code(self, manager: Manager, user_normal: UserNormalModel) -> None:
        with pytest.raises(NotFoundError) as exc_info:
            manager.remove_user(user=user_normal)
        assert exc_info.value.code == "NOT_FOUND_USER"


class TestManagerAddBook:
    @pytest.mark.unit
    def test_add_book_stores_by_id(self, manager: Manager, book_with_units: BookModel) -> None:
        manager.add_book(book=book_with_units)
        assert manager.books[book_with_units.id] is book_with_units

    @pytest.mark.unit
    def test_add_book_appears_in_books_values(self, manager: Manager, book_with_units: BookModel) -> None:
        manager.add_book(book=book_with_units)
        assert book_with_units in manager.books_values

    @pytest.mark.unit
    def test_add_book_none_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.add_book(book=None)

    @pytest.mark.unit
    def test_add_book_invalid_type_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.add_book(book="not-a-book")

    @pytest.mark.unit
    def test_add_book_validation_error_has_correct_code(self, manager: Manager) -> None:
        with pytest.raises(ValidationError) as exc_info:
            manager.add_book(book=None)
        assert exc_info.value.code == "NOT_VALID_BOOK"

    @pytest.mark.unit
    def test_add_multiple_books(self, manager: Manager, book_with_units: BookModel, book_out_of_stock: BookModel) -> None:
        manager.add_book(book=book_with_units)
        manager.add_book(book=book_out_of_stock)
        assert len(manager.books) == 2


class TestManagerRemoveBook:
    @pytest.mark.unit
    def test_remove_book_removes_from_dict(self, manager: Manager, book_with_units: BookModel) -> None:
        manager.add_book(book=book_with_units)
        manager.remove_book(book=book_with_units)
        assert book_with_units not in manager.books_values

    @pytest.mark.unit
    def test_remove_book_none_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.remove_book(book=None)

    @pytest.mark.unit
    def test_remove_book_invalid_type_raises_validation_error(self, manager: Manager) -> None:
        with pytest.raises(ValidationError):
            manager.remove_book(book="not-a-book")

    @pytest.mark.unit
    def test_remove_book_not_added_raises_not_found_error(self, manager: Manager, book_with_units: BookModel) -> None:
        with pytest.raises(NotFoundError):
            manager.remove_book(book=book_with_units)

    @pytest.mark.unit
    def test_remove_book_not_found_error_has_correct_code(self, manager: Manager, book_with_units: BookModel) -> None:
        with pytest.raises(NotFoundError) as exc_info:
            manager.remove_book(book=book_with_units)
        assert exc_info.value.code == "NOT_FOUND_BOOK"


class TestManagerRentBook:
    @pytest.mark.unit
    def test_rent_book_normal_user(self, manager: Manager, user_normal: UserNormalModel, book_with_units: BookModel) -> None:
        manager.rent_book(user=user_normal, book=book_with_units)
        assert user_normal.rented_book is book_with_units

    @pytest.mark.unit
    def test_rent_book_premium_user(self, manager: Manager, user_premium: UserPremiumModel, book_with_units: BookModel) -> None:
        manager.rent_book(user=user_premium, book=book_with_units)
        assert book_with_units in user_premium.rented_books

    @pytest.mark.unit
    def test_rent_book_invalid_user_raises_validation_error(self, manager: Manager, book_with_units: BookModel) -> None:
        with pytest.raises(ValidationError):
            manager.rent_book(user=None, book=book_with_units)

    @pytest.mark.unit
    def test_rent_book_invalid_book_raises_validation_error(self, manager: Manager, user_normal: UserNormalModel) -> None:
        with pytest.raises(ValidationError):
            manager.rent_book(user=user_normal, book=None)

    @pytest.mark.unit
    def test_rent_book_invalid_user_type_raises_validation_error(self, manager: Manager, book_with_units: BookModel) -> None:
        with pytest.raises(ValidationError):
            manager.rent_book(user="not-a-user", book=book_with_units)

    @pytest.mark.unit
    def test_rent_book_invalid_book_type_raises_validation_error(self, manager: Manager, user_normal: UserNormalModel) -> None:
        with pytest.raises(ValidationError):
            manager.rent_book(user=user_normal, book="not-a-book")

    @pytest.mark.unit
    def test_rent_book_out_of_stock_raises_business_error(self, manager: Manager, user_normal: UserNormalModel, book_out_of_stock: BookModel) -> None:
        with pytest.raises(BusinessError):
            manager.rent_book(user=user_normal, book=book_out_of_stock)


class TestManagerReturnBook:
    @pytest.mark.unit
    def test_return_book_normal_user(self, manager: Manager, user_normal: UserNormalModel, book_with_units: BookModel) -> None:
        manager.rent_book(user=user_normal, book=book_with_units)
        manager.return_book(user=user_normal)
        assert user_normal.rented_book is None

    @pytest.mark.unit
    def test_return_book_premium_user_with_book(self, manager: Manager, user_premium: UserPremiumModel, book_with_units: BookModel) -> None:
        manager.rent_book(user=user_premium, book=book_with_units)
        manager.return_book(user=user_premium, book=book_with_units)
        assert book_with_units not in user_premium.rented_books

    @pytest.mark.unit
    def test_return_book_invalid_user_raises_validation_error(self, manager: Manager, book_with_units: BookModel) -> None:
        with pytest.raises(ValidationError):
            manager.return_book(user=None, book=book_with_units)

    @pytest.mark.unit
    def test_return_book_invalid_book_type_raises_validation_error(self, manager: Manager, user_normal: UserNormalModel) -> None:
        with pytest.raises(ValidationError):
            manager.return_book(user=user_normal, book="not-a-book")

    @pytest.mark.unit
    def test_return_book_normal_user_without_rented_book_raises_not_found(self, manager: Manager, user_normal: UserNormalModel) -> None:
        with pytest.raises(NotFoundError):
            manager.return_book(user=user_normal)

    @pytest.mark.unit
    def test_return_book_premium_user_book_not_rented_raises_not_found(
        self, manager: Manager, user_premium: UserPremiumModel, book_with_units: BookModel
    ) -> None:
        with pytest.raises(NotFoundError):
            manager.return_book(user=user_premium, book=book_with_units)


class TestManagerStr:
    @pytest.mark.unit
    def test_str_contains_library_name(self, manager: Manager) -> None:
        assert "Libreria LaRosca" in str(manager)
