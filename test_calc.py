import pytest

from calc import Calc


def test_sample():
    assert 1 ==1


def test_getDivide():
    calc = Calc()
    assert calc.getDivide(4,2) == 2
    assert calc.getDivide(5,3) == 1.67

def test_getDivide_divide_by_0():
    calc = Calc()
    assert calc.getDivide(5,0)== 0.0


