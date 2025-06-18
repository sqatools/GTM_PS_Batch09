import pytest

ENV= "TEST"

def test_additin():
    num1 = 30
    num2 = 40
    assert  num1+num2 == 70

def test_multiplication():
    x = 50
    y = 7
    assert x*y == 350

@pytest.mark.skip
def test_division():
    p = 60
    q = 3
    assert p//q == 5

@pytest.mark.skipif(ENV == "PROD", reason='feature is not available in prod')
def test_subtraction():
    n= 600
    m = 200
    assert n-m == 400

