import pytest

from bookstore.utils.exceptions import (
    AuthenticationError,
    BaseError,
    BusinessError,
    ConflictError,
    InternalError,
    NotFoundError,
    ValidationError,
)


class TestBaseError:
    def test_is_exception(self) -> None:
        assert issubclass(BaseError, Exception)

    def test_default_code_is_string(self) -> None:
        error = BaseError()
        assert isinstance(error.code, str)

    def test_default_message_is_string(self) -> None:
        error = BaseError()
        assert isinstance(error.message, str)

    def test_custom_code(self) -> None:
        error = BaseError(code="ERROR_CUSTOM")
        assert error.code == "ERROR_CUSTOM"

    def test_custom_message(self) -> None:
        error = BaseError(message="Custom message.")
        assert error.message == "Custom message."

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BaseError):
            raise BaseError()


class TestValidationError:
    def test_is_base_error(self) -> None:
        assert issubclass(ValidationError, BaseError)

    def test_default_message(self) -> None:
        error = ValidationError()
        assert error.message == "Validation error"

    def test_custom_code_and_message(self) -> None:
        error = ValidationError(code="NOT_VALID_USER", message="Invalid user.")
        assert error.code == "NOT_VALID_USER"
        assert error.message == "Invalid user."

    def test_can_be_raised_and_caught_as_itself(self) -> None:
        with pytest.raises(ValidationError):
            raise ValidationError()

    def test_can_be_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise ValidationError()


class TestAuthenticationError:
    def test_is_base_error(self) -> None:
        assert issubclass(AuthenticationError, BaseError)

    def test_default_message(self) -> None:
        error = AuthenticationError()
        assert error.message == "Authentication error"

    def test_can_be_raised_and_caught_as_itself(self) -> None:
        with pytest.raises(AuthenticationError):
            raise AuthenticationError()

    def test_can_be_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise AuthenticationError()


class TestNotFoundError:
    def test_is_base_error(self) -> None:
        assert issubclass(NotFoundError, BaseError)

    def test_default_message(self) -> None:
        error = NotFoundError()
        assert error.message == "Resource not found"

    def test_custom_code_and_message(self) -> None:
        error = NotFoundError(code="NOT_FOUND_USER", message="User not found.")
        assert error.code == "NOT_FOUND_USER"
        assert error.message == "User not found."

    def test_can_be_raised_and_caught_as_itself(self) -> None:
        with pytest.raises(NotFoundError):
            raise NotFoundError()

    def test_can_be_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise NotFoundError()


class TestConflictError:
    def test_is_base_error(self) -> None:
        assert issubclass(ConflictError, BaseError)

    def test_default_message(self) -> None:
        error = ConflictError()
        assert error.message == "Conflict error"

    def test_can_be_raised_and_caught_as_itself(self) -> None:
        with pytest.raises(ConflictError):
            raise ConflictError()

    def test_can_be_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise ConflictError()


class TestBusinessError:
    def test_is_base_error(self) -> None:
        assert issubclass(BusinessError, BaseError)

    def test_default_message(self) -> None:
        error = BusinessError()
        assert error.message == "Business rule violated"

    def test_custom_code_and_message(self) -> None:
        error = BusinessError(code="ERROR_OUT_OF_STOCK", message="Book is out of stock.")
        assert error.code == "ERROR_OUT_OF_STOCK"
        assert error.message == "Book is out of stock."

    def test_can_be_raised_and_caught_as_itself(self) -> None:
        with pytest.raises(BusinessError):
            raise BusinessError()

    def test_can_be_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise BusinessError()


class TestInternalError:
    def test_is_base_error(self) -> None:
        assert issubclass(InternalError, BaseError)

    def test_default_message(self) -> None:
        error = InternalError()
        assert error.message == "Internal error"

    def test_can_be_raised_and_caught_as_itself(self) -> None:
        with pytest.raises(InternalError):
            raise InternalError()

    def test_can_be_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise InternalError()
