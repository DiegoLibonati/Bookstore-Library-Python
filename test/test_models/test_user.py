import pytest

from bookstore.models.user_model import UserModel


class TestUserAbstract:
    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            UserModel(name="Pepe", surname="Lopez", address="Calle False 123")
