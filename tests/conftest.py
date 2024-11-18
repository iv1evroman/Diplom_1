import pytest
from unittest.mock import Mock

import data


@pytest.fixture()
def mock_bun():
    mock = Mock()
    mock.name = data.BUN_NAME
    mock.price = data.BUN_PRICE
    mock.get_name.return_value = 'булка'
    mock.get_price.return_value = 100
    return mock


@pytest.fixture()
def mock_ingredient():
    mock = Mock()
    mock.type = data.INGREDIENT_TYPE
    mock.name = data.INGREDIENT_NAME
    mock.price = data.INGREDIENT_PRICE
    mock.get_type.return_value = 'соус'
    mock.get_name.return_value = 'сырный'
    mock.get_price.return_value = 50
    return mock
