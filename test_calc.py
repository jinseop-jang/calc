from calc import Calc
import pytest

def test_sample():
    assert 1 ==1

def test_get_sum():
    c = Calc()
    assert 3 == c.getSum(1, 2)

