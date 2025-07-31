import pytest

from calc import Calc


def test_sample():
    assert 1 ==1


def test_Gop():
    cal = Calc()
    ret = cal.getGop(3, 5)
    assert  ret == 15

def test_feature6():
    calc = Calc()
    assert calc.getSumSum(1,2,3) == 6


def test_getZegop():
    calc = Calc()
    for num in range(100):
        assert calc.getZegop(num) == num * num

