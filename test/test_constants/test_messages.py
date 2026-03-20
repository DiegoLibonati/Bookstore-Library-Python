from bookstore.constants.messages import (
    MESSAGE_ALREADY_EXISTS_BOOK_RENTED,
    MESSAGE_ALREADY_EXISTS_USER,
    MESSAGE_ERROR_BOOK_RETURN_REQUIRED,
    MESSAGE_ERROR_INTERNAL_LIBRARY,
    MESSAGE_ERROR_OUT_OF_STOCK,
    MESSAGE_NOT_FOUND_BOOK,
    MESSAGE_NOT_FOUND_RENTED_BOOK,
    MESSAGE_NOT_FOUND_RENTED_BOOK_BY_NAME,
    MESSAGE_NOT_FOUND_USER,
    MESSAGE_NOT_VALID_BOOK,
    MESSAGE_NOT_VALID_INTEGER,
    MESSAGE_NOT_VALID_USER,
)

ALL_MESSAGES: list[str] = [
    MESSAGE_ERROR_INTERNAL_LIBRARY,
    MESSAGE_ERROR_BOOK_RETURN_REQUIRED,
    MESSAGE_ERROR_OUT_OF_STOCK,
    MESSAGE_NOT_VALID_INTEGER,
    MESSAGE_NOT_VALID_USER,
    MESSAGE_NOT_VALID_BOOK,
    MESSAGE_ALREADY_EXISTS_BOOK_RENTED,
    MESSAGE_ALREADY_EXISTS_USER,
    MESSAGE_NOT_FOUND_BOOK,
    MESSAGE_NOT_FOUND_RENTED_BOOK,
    MESSAGE_NOT_FOUND_RENTED_BOOK_BY_NAME,
    MESSAGE_NOT_FOUND_USER,
]

MESSAGES_WITH_NAME_PLACEHOLDER: list[str] = [
    MESSAGE_ERROR_BOOK_RETURN_REQUIRED,
    MESSAGE_ERROR_OUT_OF_STOCK,
    MESSAGE_ALREADY_EXISTS_BOOK_RENTED,
    MESSAGE_NOT_FOUND_BOOK,
    MESSAGE_NOT_FOUND_RENTED_BOOK_BY_NAME,
]


class TestMessagesType:
    def test_all_messages_are_strings(self) -> None:
        for message in ALL_MESSAGES:
            assert isinstance(message, str)

    def test_all_messages_are_non_empty(self) -> None:
        for message in ALL_MESSAGES:
            assert len(message) > 0


class TestMessagesFormat:
    def test_messages_with_name_placeholder_are_formattable(self) -> None:
        for message in MESSAGES_WITH_NAME_PLACEHOLDER:
            formatted = message.format(name="Test Book")
            assert "Test Book" in formatted

    def test_message_error_book_return_required_contains_name(self) -> None:
        formatted = MESSAGE_ERROR_BOOK_RETURN_REQUIRED.format(name="Drácula")
        assert "Drácula" in formatted

    def test_message_error_out_of_stock_contains_name(self) -> None:
        formatted = MESSAGE_ERROR_OUT_OF_STOCK.format(name="Drácula")
        assert "Drácula" in formatted

    def test_message_already_exists_book_rented_contains_name(self) -> None:
        formatted = MESSAGE_ALREADY_EXISTS_BOOK_RENTED.format(name="Drácula")
        assert "Drácula" in formatted

    def test_message_not_found_book_contains_name(self) -> None:
        formatted = MESSAGE_NOT_FOUND_BOOK.format(name="Drácula")
        assert "Drácula" in formatted

    def test_message_not_found_rented_book_by_name_contains_name(self) -> None:
        formatted = MESSAGE_NOT_FOUND_RENTED_BOOK_BY_NAME.format(name="Drácula")
        assert "Drácula" in formatted
