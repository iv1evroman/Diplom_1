import data
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        burger = Burger()
        bun = Bun(data.BUN_NAME, data.BUN_PRICE)
        burger.set_buns(bun)
        assert burger.bun.get_name() == 'булка' and burger.bun.get_price() == 100

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(data.INGREDIENT_TYPE, data.INGREDIENT_NAME, data.INGREDIENT_PRICE)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0].__dict__ == {'type': 'соус', 'name': 'сырный', 'price': 50}

    def test_get_price(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == 250

    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_