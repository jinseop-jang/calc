import pytest

from calc import Calc


def test_get_minus():
    calc = Calc()
    assert calc.get_minus(7, 2) == 5
    assert calc.get_minus(2, 7) == -5