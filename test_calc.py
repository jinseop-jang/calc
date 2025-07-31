from calc import Calc
import pytest

from calc import Calc


def test_get_minus():
    calc = Calc()
    assert calc.get_minus(7, 2) == 5
    assert calc.get_minus(2, 7) == -5

def test_getDivide():
    calc = Calc()
    assert calc.getDivide(4,2) == 2
    assert calc.getDivide(5,3) == 1.67

def test_getDivide_divide_by_0():
    calc = Calc()
    assert calc.getDivide(5,0)== 0.0


def test_sample():
    assert 1 ==1

def test_get_sum():
    c = Calc()
    assert 3 == c.getSum(1, 2)

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

