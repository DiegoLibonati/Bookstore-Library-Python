import pytest

import lend_book.constants.codes as codes


class TestCodes:
    @pytest.mark.unit
    def test_code_error_internal_library(self) -> None:
        assert codes.CODE_ERROR_INTERNAL_LIBRARY == "ERROR_INTERNAL_LIBRARY"

    @pytest.mark.unit
    def test_code_error_book_return_required(self) -> None:
        assert codes.CODE_ERROR_BOOK_RETURN_REQUIRED == "ERROR_BOOK_RETURN_REQUIRED"

    @pytest.mark.unit
    def test_code_error_out_of_stock(self) -> None:
        assert codes.CODE_ERROR_OUT_OF_STOCK == "ERROR_OUT_OF_STOCK"

    @pytest.mark.unit
    def test_code_not_valid_integer(self) -> None:
        assert codes.CODE_NOT_VALID_INTEGER == "NOT_VALID_INTEGER"

    @pytest.mark.unit
    def test_code_not_valid_user(self) -> None:
        assert codes.CODE_NOT_VALID_USER == "NOT_VALID_USER"

    @pytest.mark.unit
    def test_code_not_valid_book(self) -> None:
        assert codes.CODE_NOT_VALID_BOOK == "NOT_VALID_BOOK"

    @pytest.mark.unit
    def test_code_already_exists_book_rented(self) -> None:
        assert codes.CODE_ALREADY_EXISTS_BOOK_RENTED == "ALREADY_EXISTS_BOOK_RENTED"

    @pytest.mark.unit
    def test_code_already_exists_user(self) -> None:
        assert codes.CODE_ALREADY_EXISTS_USER == "ALREADY_EXISTS_USER"

    @pytest.mark.unit
    def test_code_not_found_book(self) -> None:
        assert codes.CODE_NOT_FOUND_BOOK == "NOT_FOUND_BOOK"

    @pytest.mark.unit
    def test_code_not_found_rented_book(self) -> None:
        assert codes.CODE_NOT_FOUND_RENTED_BOOK == "NOT_FOUND_RENTED_BOOK"

    @pytest.mark.unit
    def test_code_not_found_user(self) -> None:
        assert codes.CODE_NOT_FOUND_USER == "NOT_FOUND_USER"

    @pytest.mark.unit
    def test_all_codes_are_strings(self) -> None:
        all_codes: list[str] = [
            codes.CODE_ERROR_INTERNAL_LIBRARY,
            codes.CODE_ERROR_BOOK_RETURN_REQUIRED,
            codes.CODE_ERROR_OUT_OF_STOCK,
            codes.CODE_NOT_VALID_INTEGER,
            codes.CODE_NOT_VALID_USER,
            codes.CODE_NOT_VALID_BOOK,
            codes.CODE_ALREADY_EXISTS_BOOK_RENTED,
            codes.CODE_ALREADY_EXISTS_USER,
            codes.CODE_NOT_FOUND_BOOK,
            codes.CODE_NOT_FOUND_RENTED_BOOK,
            codes.CODE_NOT_FOUND_USER,
        ]
        for code in all_codes:
            assert isinstance(code, str)

    @pytest.mark.unit
    def test_all_codes_are_unique(self) -> None:
        all_codes: list[str] = [
            codes.CODE_ERROR_INTERNAL_LIBRARY,
            codes.CODE_ERROR_BOOK_RETURN_REQUIRED,
            codes.CODE_ERROR_OUT_OF_STOCK,
            codes.CODE_NOT_VALID_INTEGER,
            codes.CODE_NOT_VALID_USER,
            codes.CODE_NOT_VALID_BOOK,
            codes.CODE_ALREADY_EXISTS_BOOK_RENTED,
            codes.CODE_ALREADY_EXISTS_USER,
            codes.CODE_NOT_FOUND_BOOK,
            codes.CODE_NOT_FOUND_RENTED_BOOK,
            codes.CODE_NOT_FOUND_USER,
        ]
        assert len(all_codes) == len(set(all_codes))
