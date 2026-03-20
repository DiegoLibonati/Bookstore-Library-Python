from bookstore.constants.codes import (
    CODE_ALREADY_EXISTS_BOOK_RENTED,
    CODE_ALREADY_EXISTS_USER,
    CODE_ERROR_BOOK_RETURN_REQUIRED,
    CODE_ERROR_INTERNAL_LIBRARY,
    CODE_ERROR_OUT_OF_STOCK,
    CODE_NOT_FOUND_BOOK,
    CODE_NOT_FOUND_RENTED_BOOK,
    CODE_NOT_FOUND_USER,
    CODE_NOT_VALID_BOOK,
    CODE_NOT_VALID_INTEGER,
    CODE_NOT_VALID_USER,
)

ALLOWED_PREFIXES: tuple[str, ...] = ("SUCCESS_", "ERROR_", "NOT_VALID_", "NOT_EXISTS_", "ALREADY_EXISTS_", "NOT_FOUND_")

ALL_CODES: list[str] = [
    CODE_ERROR_INTERNAL_LIBRARY,
    CODE_ERROR_BOOK_RETURN_REQUIRED,
    CODE_ERROR_OUT_OF_STOCK,
    CODE_NOT_VALID_INTEGER,
    CODE_NOT_VALID_USER,
    CODE_NOT_VALID_BOOK,
    CODE_ALREADY_EXISTS_BOOK_RENTED,
    CODE_ALREADY_EXISTS_USER,
    CODE_NOT_FOUND_BOOK,
    CODE_NOT_FOUND_RENTED_BOOK,
    CODE_NOT_FOUND_USER,
]


class TestCodesType:
    def test_all_codes_are_strings(self) -> None:
        for code in ALL_CODES:
            assert isinstance(code, str)

    def test_all_codes_are_non_empty(self) -> None:
        for code in ALL_CODES:
            assert len(code) > 0


class TestCodesPrefix:
    def test_all_codes_have_valid_prefix(self) -> None:
        for code in ALL_CODES:
            assert code.startswith(ALLOWED_PREFIXES), f"Code '{code}' does not start with an allowed prefix"

    def test_error_codes_have_error_prefix(self) -> None:
        error_codes: list[str] = [CODE_ERROR_INTERNAL_LIBRARY, CODE_ERROR_BOOK_RETURN_REQUIRED, CODE_ERROR_OUT_OF_STOCK]
        for code in error_codes:
            assert code.startswith("ERROR_")

    def test_not_valid_codes_have_not_valid_prefix(self) -> None:
        not_valid_codes: list[str] = [CODE_NOT_VALID_INTEGER, CODE_NOT_VALID_USER, CODE_NOT_VALID_BOOK]
        for code in not_valid_codes:
            assert code.startswith("NOT_VALID_")

    def test_already_exists_codes_have_already_exists_prefix(self) -> None:
        already_exists_codes: list[str] = [CODE_ALREADY_EXISTS_BOOK_RENTED, CODE_ALREADY_EXISTS_USER]
        for code in already_exists_codes:
            assert code.startswith("ALREADY_EXISTS_")

    def test_not_found_codes_have_not_found_prefix(self) -> None:
        not_found_codes: list[str] = [CODE_NOT_FOUND_BOOK, CODE_NOT_FOUND_RENTED_BOOK, CODE_NOT_FOUND_USER]
        for code in not_found_codes:
            assert code.startswith("NOT_FOUND_")


class TestCodesValues:
    def test_code_error_internal_library(self) -> None:
        assert CODE_ERROR_INTERNAL_LIBRARY == "ERROR_INTERNAL_LIBRARY"

    def test_code_error_book_return_required(self) -> None:
        assert CODE_ERROR_BOOK_RETURN_REQUIRED == "ERROR_BOOK_RETURN_REQUIRED"

    def test_code_error_out_of_stock(self) -> None:
        assert CODE_ERROR_OUT_OF_STOCK == "ERROR_OUT_OF_STOCK"

    def test_code_not_valid_integer(self) -> None:
        assert CODE_NOT_VALID_INTEGER == "NOT_VALID_INTEGER"

    def test_code_not_valid_user(self) -> None:
        assert CODE_NOT_VALID_USER == "NOT_VALID_USER"

    def test_code_not_valid_book(self) -> None:
        assert CODE_NOT_VALID_BOOK == "NOT_VALID_BOOK"

    def test_code_already_exists_book_rented(self) -> None:
        assert CODE_ALREADY_EXISTS_BOOK_RENTED == "ALREADY_EXISTS_BOOK_RENTED"

    def test_code_already_exists_user(self) -> None:
        assert CODE_ALREADY_EXISTS_USER == "ALREADY_EXISTS_USER"

    def test_code_not_found_book(self) -> None:
        assert CODE_NOT_FOUND_BOOK == "NOT_FOUND_BOOK"

    def test_code_not_found_rented_book(self) -> None:
        assert CODE_NOT_FOUND_RENTED_BOOK == "NOT_FOUND_RENTED_BOOK"

    def test_code_not_found_user(self) -> None:
        assert CODE_NOT_FOUND_USER == "NOT_FOUND_USER"
