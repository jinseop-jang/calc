import pytest
from calc import Calc

def test_sample():
    assert 1 ==1


def test_feature6():
    calc = Calc()
    assert calc.getSumSum(1,2,3) == 6

