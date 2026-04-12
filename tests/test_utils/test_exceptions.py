import pytest

from lend_book.utils.exceptions import (
    AuthenticationError,
    BaseError,
    BusinessError,
    ConflictError,
    InternalError,
    NotFoundError,
    ValidationError,
)


class TestBaseError:
    @pytest.mark.unit
    def test_is_exception_subclass(self) -> None:
        assert issubclass(BaseError, Exception)

    @pytest.mark.unit
    def test_default_code(self) -> None:
        error: BaseError = BaseError()
        assert error.code == "ERROR_INTERNAL_LIBRARY"

    @pytest.mark.unit
    def test_default_message_is_set(self) -> None:
        error: BaseError = BaseError()
        assert error.message is not None
        assert len(error.message) > 0

    @pytest.mark.unit
    def test_custom_message(self) -> None:
        error: BaseError = BaseError(message="Custom error message")
        assert error.message == "Custom error message"

    @pytest.mark.unit
    def test_custom_code(self) -> None:
        error: BaseError = BaseError(code="CUSTOM_CODE")
        assert error.code == "CUSTOM_CODE"

    @pytest.mark.unit
    def test_custom_code_and_message(self) -> None:
        error: BaseError = BaseError(code="MY_CODE", message="My message")
        assert error.code == "MY_CODE"
        assert error.message == "My message"

    @pytest.mark.unit
    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BaseError):
            raise BaseError()

    @pytest.mark.unit
    def test_args_contains_message(self) -> None:
        error: BaseError = BaseError(message="Test message")
        assert "Test message" in error.args


class TestValidationError:
    @pytest.mark.unit
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(ValidationError, BaseError)

    @pytest.mark.unit
    def test_is_exception_subclass(self) -> None:
        assert issubclass(ValidationError, Exception)

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise ValidationError()

    @pytest.mark.unit
    def test_custom_code_and_message(self) -> None:
        error: ValidationError = ValidationError(code="NOT_VALID_USER", message="User is invalid")
        assert error.code == "NOT_VALID_USER"
        assert error.message == "User is invalid"


class TestAuthenticationError:
    @pytest.mark.unit
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(AuthenticationError, BaseError)

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise AuthenticationError()

    @pytest.mark.unit
    def test_custom_code_and_message(self) -> None:
        error: AuthenticationError = AuthenticationError(code="AUTH_FAILED", message="Unauthorized")
        assert error.code == "AUTH_FAILED"
        assert error.message == "Unauthorized"


class TestNotFoundError:
    @pytest.mark.unit
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(NotFoundError, BaseError)

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise NotFoundError()

    @pytest.mark.unit
    def test_custom_code_and_message(self) -> None:
        error: NotFoundError = NotFoundError(code="NOT_FOUND_BOOK", message="Book not found")
        assert error.code == "NOT_FOUND_BOOK"
        assert error.message == "Book not found"


class TestConflictError:
    @pytest.mark.unit
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(ConflictError, BaseError)

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise ConflictError()

    @pytest.mark.unit
    def test_custom_code_and_message(self) -> None:
        error: ConflictError = ConflictError(code="ALREADY_EXISTS_USER", message="User already exists")
        assert error.code == "ALREADY_EXISTS_USER"
        assert error.message == "User already exists"


class TestBusinessError:
    @pytest.mark.unit
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(BusinessError, BaseError)

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise BusinessError()

    @pytest.mark.unit
    def test_custom_code_and_message(self) -> None:
        error: BusinessError = BusinessError(code="ERROR_OUT_OF_STOCK", message="Out of stock")
        assert error.code == "ERROR_OUT_OF_STOCK"
        assert error.message == "Out of stock"


class TestInternalError:
    @pytest.mark.unit
    def test_is_base_error_subclass(self) -> None:
        assert issubclass(InternalError, BaseError)

    @pytest.mark.unit
    def test_can_be_raised_and_caught_as_base_error(self) -> None:
        with pytest.raises(BaseError):
            raise InternalError()

    @pytest.mark.unit
    def test_custom_code_and_message(self) -> None:
        error: InternalError = InternalError(code="INTERNAL_FAIL", message="Unexpected failure")
        assert error.code == "INTERNAL_FAIL"
        assert error.message == "Unexpected failure"
