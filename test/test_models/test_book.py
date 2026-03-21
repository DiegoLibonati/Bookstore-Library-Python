from bookstore.models.book_model import BookModel


class TestBookInit:
    def test_id_is_string(self, book: BookModel) -> None:
        assert isinstance(book.id, str)

    def test_id_is_non_empty(self, book: BookModel) -> None:
        assert len(book.id) > 0

    def test_name(self, book: BookModel) -> None:
        assert book.name == "Drácula"

    def test_description(self, book: BookModel) -> None:
        assert book.description == "Novela gótica de Bram Stoker."

    def test_author(self, book: BookModel) -> None:
        assert book.author == "Bram Stoker"

    def test_units(self, book: BookModel) -> None:
        assert book.units == 5

    def test_banner_url_default_is_empty_string(self, book: BookModel) -> None:
        assert book.banner_url == ""

    def test_banner_url_custom(self) -> None:
        b = BookModel(name="X", description="Y", author="Z", units=1, banner_url="http://example.com/img.jpg")
        assert b.banner_url == "http://example.com/img.jpg"

    def test_each_instance_has_unique_id(self) -> None:
        b1 = BookModel(name="A", description="A", author="A", units=1)
        b2 = BookModel(name="A", description="A", author="A", units=1)
        assert b1.id != b2.id


class TestBookStock:
    def test_stock_is_true_when_units_above_zero(self, book: BookModel) -> None:
        assert book.stock is True

    def test_stock_is_false_when_units_zero(self, book_no_stock: BookModel) -> None:
        assert book_no_stock.stock is False

    def test_stock_is_bool(self, book: BookModel) -> None:
        assert isinstance(book.stock, bool)


class TestBookDecreaseUnit:
    def test_decrease_unit_reduces_by_one(self, book: BookModel) -> None:
        initial_units = book.units
        book.decrease_unit()
        assert book.units == initial_units - 1

    def test_decrease_unit_sets_zero_when_last_unit(self) -> None:
        b = BookModel(name="X", description="Y", author="Z", units=1)
        b.decrease_unit()
        assert b.units == 0

    def test_decrease_unit_does_nothing_when_out_of_stock(self, book_no_stock: BookModel) -> None:
        book_no_stock.decrease_unit()
        assert book_no_stock.units == 0

    def test_stock_becomes_false_after_last_unit_decreased(self) -> None:
        b = BookModel(name="X", description="Y", author="Z", units=1)
        b.decrease_unit()
        assert b.stock is False


class TestBookIncreaseUnit:
    def test_increase_unit_adds_one(self, book: BookModel) -> None:
        initial_units = book.units
        book.increase_unit()
        assert book.units == initial_units + 1

    def test_increase_unit_from_zero(self, book_no_stock: BookModel) -> None:
        book_no_stock.increase_unit()
        assert book_no_stock.units == 1

    def test_stock_becomes_true_after_increase_from_zero(self, book_no_stock: BookModel) -> None:
        book_no_stock.increase_unit()
        assert book_no_stock.stock is True


class TestBookBannerUrl:
    def test_banner_url_setter(self, book: BookModel) -> None:
        book.banner_url = "http://example.com/dracula.jpg"
        assert book.banner_url == "http://example.com/dracula.jpg"

    def test_banner_url_setter_overwrites_previous(self, book: BookModel) -> None:
        book.banner_url = "http://first.com/img.jpg"
        book.banner_url = "http://second.com/img.jpg"
        assert book.banner_url == "http://second.com/img.jpg"


class TestBookStr:
    def test_str_returns_string(self, book: BookModel) -> None:
        assert isinstance(str(book), str)

    def test_str_contains_id(self, book: BookModel) -> None:
        assert book.id in str(book)

    def test_str_contains_name(self, book: BookModel) -> None:
        assert book.name in str(book)

    def test_str_contains_author(self, book: BookModel) -> None:
        assert book.author in str(book)

    def test_str_contains_units(self, book: BookModel) -> None:
        assert str(book.units) in str(book)
