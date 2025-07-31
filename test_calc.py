import pytest

from calc import Calc


def test_sample():
    assert 1 ==1

def test_Gop():
    cal = Calc()
    ret = cal.getGop(3, 5)
    assert  ret == 15