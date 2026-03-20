import pytest

from bookstore.manager import Manager
from bookstore.models.book import Book
from bookstore.models.user_normal import UserNormal
from bookstore.models.user_premium import UserPremium


@pytest.fixture
def book() -> Book:
    return Book(name="Drácula", description="Novela gótica de Bram Stoker.", author="Bram Stoker", units=5)


@pytest.fixture
def book_no_stock() -> Book:
    return Book(name="Sin Stock", description="Libro sin stock.", author="Autor Desconocido", units=0)


@pytest.fixture
def book_secondary() -> Book:
    return Book(name="Gravity Falls", description="Libro misterioso.", author="Alex Hirsch", units=3)


@pytest.fixture
def user_normal() -> UserNormal:
    return UserNormal(name="Pepe", surname="Alcachofaz", address="Calle False 123")


@pytest.fixture
def user_premium() -> UserPremium:
    return UserPremium(name="Carlos", surname="Skere", address="Calle False 1234")


@pytest.fixture
def manager() -> Manager:
    return Manager(name="Libreria Test")
