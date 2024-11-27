class TestBun:
    def test_get_name_of_bun(self, mock_bun):
        bun = mock_bun
        assert bun.get_name() == 'булка'

    def test_get_price_of_bun(self, mock_bun):
        bun = mock_bun
        assert bun.get_price() == 100