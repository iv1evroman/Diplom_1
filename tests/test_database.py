from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()
        assert database.available_buns()[1].__dict__ == {'name': 'white bun', 'price': 200}

    def test_available_ingredients(self):
        database = Database()
        assert database.available_ingredients()[4].__dict__ == {'type': 'FILLING', 'name': 'dinosaur', 'price': 200}