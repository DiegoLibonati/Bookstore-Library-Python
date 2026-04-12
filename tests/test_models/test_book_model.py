import pytest

from lend_book.models.book_model import BookModel


class TestBookModelInit:
    @pytest.mark.unit
    def test_id_is_string(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=3)
        assert isinstance(book.id, str)

    @pytest.mark.unit
    def test_id_is_not_empty(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=3)
        assert len(book.id) > 0

    @pytest.mark.unit
    def test_name_property(self) -> None:
        book: BookModel = BookModel(name="Drácula", description="Desc", author="Bram Stoker", units=10)
        assert book.name == "Drácula"

    @pytest.mark.unit
    def test_description_property(self) -> None:
        book: BookModel = BookModel(name="Test", description="A gothic novel.", author="Author", units=5)
        assert book.description == "A gothic novel."

    @pytest.mark.unit
    def test_author_property(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Bram Stoker", units=5)
        assert book.author == "Bram Stoker"

    @pytest.mark.unit
    def test_units_property(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=7)
        assert book.units == 7

    @pytest.mark.unit
    def test_banner_url_defaults_to_empty_string(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=3)
        assert book.banner_url == ""

    @pytest.mark.unit
    def test_banner_url_with_explicit_value(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=3, banner_url="http://img.png")
        assert book.banner_url == "http://img.png"

    @pytest.mark.unit
    def test_two_books_have_different_ids(self) -> None:
        book_a: BookModel = BookModel(name="A", description="Desc", author="Author", units=1)
        book_b: BookModel = BookModel(name="B", description="Desc", author="Author", units=1)
        assert book_a.id != book_b.id


class TestBookModelStock:
    @pytest.mark.unit
    def test_stock_true_when_units_positive(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=3)
        assert book.stock is True

    @pytest.mark.unit
    def test_stock_false_when_units_zero(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=0)
        assert book.stock is False

    @pytest.mark.unit
    def test_stock_true_when_units_is_one(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=1)
        assert book.stock is True


class TestBookModelBannerUrlSetter:
    @pytest.mark.unit
    def test_setter_updates_banner_url(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=3)
        book.banner_url = "http://new-url.png"
        assert book.banner_url == "http://new-url.png"

    @pytest.mark.unit
    def test_setter_can_clear_banner_url(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=3, banner_url="http://img.png")
        book.banner_url = ""
        assert book.banner_url == ""


class TestBookModelDecreaseUnit:
    @pytest.mark.unit
    def test_decrease_unit_decrements_by_one(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=5)
        book.decrease_unit()
        assert book.units == 4

    @pytest.mark.unit
    def test_decrease_unit_from_one_sets_zero(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=1)
        book.decrease_unit()
        assert book.units == 0

    @pytest.mark.unit
    def test_decrease_unit_when_out_of_stock_does_nothing(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=0)
        book.decrease_unit()
        assert book.units == 0

    @pytest.mark.unit
    def test_decrease_unit_sets_stock_to_false_when_last_unit(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=1)
        book.decrease_unit()
        assert book.stock is False

    @pytest.mark.unit
    def test_decrease_unit_multiple_times(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=3)
        book.decrease_unit()
        book.decrease_unit()
        assert book.units == 1


class TestBookModelIncreaseUnit:
    @pytest.mark.unit
    def test_increase_unit_increments_by_one(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=3)
        book.increase_unit()
        assert book.units == 4

    @pytest.mark.unit
    def test_increase_unit_from_zero_sets_stock_true(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=0)
        book.increase_unit()
        assert book.units == 1
        assert book.stock is True

    @pytest.mark.unit
    def test_increase_unit_multiple_times(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=0)
        book.increase_unit()
        book.increase_unit()
        assert book.units == 2


class TestBookModelStr:
    @pytest.mark.unit
    def test_str_contains_book_id(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=3)
        assert book.id in str(book)

    @pytest.mark.unit
    def test_str_contains_book_name(self) -> None:
        book: BookModel = BookModel(name="Drácula", description="Desc", author="Author", units=3)
        assert "Drácula" in str(book)

    @pytest.mark.unit
    def test_str_contains_author(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Bram Stoker", units=3)
        assert "Bram Stoker" in str(book)

    @pytest.mark.unit
    def test_str_contains_units(self) -> None:
        book: BookModel = BookModel(name="Test", description="Desc", author="Author", units=3)
        assert "3" in str(book)
