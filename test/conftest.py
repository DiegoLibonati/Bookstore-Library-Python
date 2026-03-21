import pytest

from bookstore.manager import Manager
from bookstore.models.book_model import BookModel
from bookstore.models.user_normal_model import UserNormalModel
from bookstore.models.user_premium_model import UserPremiumModel


@pytest.fixture
def book() -> BookModel:
    return BookModel(name="Drácula", description="Novela gótica de Bram Stoker.", author="Bram Stoker", units=5)


@pytest.fixture
def book_no_stock() -> BookModel:
    return BookModel(name="Sin Stock", description="Libro sin stock.", author="Autor Desconocido", units=0)


@pytest.fixture
def book_secondary() -> BookModel:
    return BookModel(name="Gravity Falls", description="Libro misterioso.", author="Alex Hirsch", units=3)


@pytest.fixture
def user_normal() -> UserNormalModel:
    return UserNormalModel(name="Pepe", surname="Alcachofaz", address="Calle False 123")


@pytest.fixture
def user_premium() -> UserPremiumModel:
    return UserPremiumModel(name="Carlos", surname="Skere", address="Calle False 1234")


@pytest.fixture
def manager() -> Manager:
    return Manager(name="Libreria Test")
