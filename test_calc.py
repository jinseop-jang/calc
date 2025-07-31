import pytest

from calc import Calc


def test_sample():
    assert 1 ==1

def test_getZegop():
    calc = Calc()
    for num in range(100):
        assert calc.getZegop(num) == num * num
