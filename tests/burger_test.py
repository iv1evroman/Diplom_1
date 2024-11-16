from bun import Bun
from praktikum import main
from burger import Burger
from database import Database
from typing import List



class TestBurger:
    def test_set_bun(self):
        burger = Burger()
        buns: List[Bun] = list[(Bun('булка', 100))]
        assert burger.set_buns(buns[0]) == 'булка', 100