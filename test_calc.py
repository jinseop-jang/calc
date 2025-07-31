import pytest

from calc import Calc


def test_sample():
    assert 1 ==1


def test_getDivide():
    calc = Calc()
    assert calc.getDivide(4,2) == 2


