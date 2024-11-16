from bun import Bun


class TestBun:
    def test_get_name_of_bun(self):
        bun = Bun('булка', 0)
        assert bun.get_name() == 'булка'

    def test_get_price_of_bun(self):
        bun = Bun('булка', 100500)
        assert bun.get_price() == 100500