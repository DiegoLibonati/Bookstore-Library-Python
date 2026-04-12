import pytest

from lend_book.manager import Manager
from lend_book.models.book_model import BookModel
from lend_book.models.user_normal_model import UserNormalModel
from lend_book.models.user_premium_model import UserPremiumModel


@pytest.fixture(scope="function")
def book_with_units() -> BookModel:
    return BookModel(name="Drácula", description="Novela gótica de Bram Stoker.", author="Bram Stoker", units=5)


@pytest.fixture(scope="function")
def book_out_of_stock() -> BookModel:
    return BookModel(name="Gravity Falls", description="Libro de datos escalofriantes.", author="Alex Hirsch", units=0)


@pytest.fixture(scope="function")
def user_normal() -> UserNormalModel:
    return UserNormalModel(name="Pepe", surname="Alcachofaz", address="Calle False 123")


@pytest.fixture(scope="function")
def user_premium() -> UserPremiumModel:
    return UserPremiumModel(name="Carlos", surname="Skere", address="Calle False 1234")


@pytest.fixture(scope="function")
def manager() -> Manager:
    return Manager(name="Libreria LaRosca")
