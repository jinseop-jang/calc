from calc import Calc
import pytest

def test_sample():
    assert 1 ==1

def test_get_sum():
    c = Calc()
    assert 3 == c.getSum(1, 2)

def test_feature6():
    calc = Calc()
    assert calc.getSumSum(1,2,3) == 6


def test_getZegop():
    calc = Calc()
    for num in range(100):
        assert calc.getZegop(num) == num * num
