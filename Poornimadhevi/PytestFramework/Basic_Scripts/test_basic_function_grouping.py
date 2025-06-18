import pytest

@pytest.mark.smoke
def test_addition():
    num1 = 30
    num2 = 40
    assert  num1+num2 == 70

@pytest.mark.smoke
def test_multiplication():
    x = 50
    y = 7
    assert x*y == 350

@pytest.mark.smoke
def test_division():
    p = 60
    q = 3
    assert p//q == 5

@pytest.mark.sanity
def test_subtraction():
    n= 600
    m = 200
    assert n-m == 400

@pytest.mark.sanity
def test_addition1():
    num1 = 30
    num2 = 40
    assert  num1+num2 == 70

@pytest.mark.sanity
def test_multiplication1():
    x = 50
    y = 7
    assert x*y == 350

@pytest.mark.regression
def test_division1():
    p = 60
    q = 3
    assert p//q == 5

@pytest.mark.regression
def test_subtraction1():
    n= 600
    m = 200
    assert n-m == 400

@pytest.mark.regression
def test_addition2():
    num1 = 30
    num2 = 40
    assert  num1+num2 == 70

@pytest.mark.smoke
@pytest.mark.sanity
def test_multiplication2():
    x = 50
    y = 7
    assert x*y == 350

@pytest.mark.sanity
@pytest.mark.regression
def test_division2():
    p = 60
    q = 3
    assert p//q == 5

@pytest.mark.smoke
@pytest.mark.regression
def test_subtraction2():
    n= 600
    m = 200
    assert n-m == 400
