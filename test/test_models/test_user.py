import pytest

from bookstore.models.user import User


class TestUserAbstract:
    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            User(name="Pepe", surname="Lopez", address="Calle False 123")
