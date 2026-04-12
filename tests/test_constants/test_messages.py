import pytest

import lend_book.constants.messages as messages


class TestMessages:
    @pytest.mark.unit
    def test_message_error_internal_library_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_ERROR_INTERNAL_LIBRARY, str)

    @pytest.mark.unit
    def test_message_error_book_return_required_format(self) -> None:
        result: str = messages.MESSAGE_ERROR_BOOK_RETURN_REQUIRED.format(name="Drácula")
        assert "Drácula" in result

    @pytest.mark.unit
    def test_message_error_out_of_stock_format(self) -> None:
        result: str = messages.MESSAGE_ERROR_OUT_OF_STOCK.format(name="Gravity Falls")
        assert "Gravity Falls" in result

    @pytest.mark.unit
    def test_message_not_valid_integer_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_INTEGER, str)

    @pytest.mark.unit
    def test_message_not_valid_user_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_USER, str)

    @pytest.mark.unit
    def test_message_not_valid_book_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_VALID_BOOK, str)

    @pytest.mark.unit
    def test_message_already_exists_book_rented_format(self) -> None:
        result: str = messages.MESSAGE_ALREADY_EXISTS_BOOK_RENTED.format(name="Drácula")
        assert "Drácula" in result

    @pytest.mark.unit
    def test_message_already_exists_user_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_ALREADY_EXISTS_USER, str)

    @pytest.mark.unit
    def test_message_not_found_book_format(self) -> None:
        result: str = messages.MESSAGE_NOT_FOUND_BOOK.format(name="Gravity Falls")
        assert "Gravity Falls" in result

    @pytest.mark.unit
    def test_message_not_found_rented_book_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_FOUND_RENTED_BOOK, str)

    @pytest.mark.unit
    def test_message_not_found_rented_book_by_name_format(self) -> None:
        result: str = messages.MESSAGE_NOT_FOUND_RENTED_BOOK_BY_NAME.format(name="Drácula")
        assert "Drácula" in result

    @pytest.mark.unit
    def test_message_not_found_user_is_string(self) -> None:
        assert isinstance(messages.MESSAGE_NOT_FOUND_USER, str)

    @pytest.mark.unit
    def test_all_messages_are_non_empty(self) -> None:
        all_messages: list[str] = [
            messages.MESSAGE_ERROR_INTERNAL_LIBRARY,
            messages.MESSAGE_ERROR_BOOK_RETURN_REQUIRED,
            messages.MESSAGE_ERROR_OUT_OF_STOCK,
            messages.MESSAGE_NOT_VALID_INTEGER,
            messages.MESSAGE_NOT_VALID_USER,
            messages.MESSAGE_NOT_VALID_BOOK,
            messages.MESSAGE_ALREADY_EXISTS_BOOK_RENTED,
            messages.MESSAGE_ALREADY_EXISTS_USER,
            messages.MESSAGE_NOT_FOUND_BOOK,
            messages.MESSAGE_NOT_FOUND_RENTED_BOOK,
            messages.MESSAGE_NOT_FOUND_RENTED_BOOK_BY_NAME,
            messages.MESSAGE_NOT_FOUND_USER,
        ]
        for msg in all_messages:
            assert len(msg) > 0
