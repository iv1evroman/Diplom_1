import pytest

from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        assert database.available_buns()[1].__dict__ == {'name': 'white bun', 'price': 200}

    @pytest.mark.parametrize(
        'number,ingredient',
        [
            [1, {'type': 'SAUCE', 'name': 'sour cream', 'price': 200}],
            [4, {'type': 'FILLING', 'name': 'dinosaur', 'price': 200}]
        ]
    )
    def test_available_ingredients(self, number, ingredient):
        database = Database()
        assert database.available_ingredients()[number].__dict__ == ingredient
