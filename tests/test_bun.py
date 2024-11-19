import pytest

import data
from praktikum.bun import Bun


class TestBun:
    def test_get_name_of_bun(self):
        bun = Bun(data.BUN_NAME, data.BUN_PRICE)
        assert bun.get_name() == 'булка'

    def test_get_price_of_bun(self):
        bun = Bun(data.BUN_NAME, data.BUN_PRICE)
        assert bun.get_price() == 100