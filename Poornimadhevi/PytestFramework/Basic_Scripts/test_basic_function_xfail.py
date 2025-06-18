import pytest


def test_addition():
    num1 = 30
    num2 = 40
    assert num1 + num2 == 70

@pytest.mark.xfail
def test_multiplication():
    x = 50
    y = 7
    assert x * y == 350


@pytest.mark.xfail
def test_division():
    p = 60
    q = 3
    assert p // q == 5


def test_subtraction():
    n = 600
    m = 200
    assert n - m == 400
