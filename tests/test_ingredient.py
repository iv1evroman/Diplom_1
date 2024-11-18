import data
from praktikum.ingredient import Ingredient


class TestIngredient:
    def test_get_type_of_bun(self):
        ingredient = Ingredient(data.INGREDIENT_TYPE, data.INGREDIENT_NAME, data.INGREDIENT_PRICE)
        assert ingredient.get_type() == 'соус'

    def test_get_name_of_bun(self):
        ingredient = Ingredient(data.INGREDIENT_TYPE, data.INGREDIENT_NAME, data.INGREDIENT_PRICE)
        assert ingredient.get_name() == 'сырный'

    def test_get_price_of_bun(self):
        ingredient = Ingredient(data.INGREDIENT_TYPE, data.INGREDIENT_NAME, data.INGREDIENT_PRICE)
        assert ingredient.get_price() == 50