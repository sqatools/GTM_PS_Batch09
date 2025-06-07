"""
Scope of fixtures:

function scope : function level fixture will execute before each test function execution.
module scope :  module level fixture will execute before entire module test cases execution.
package scope : package level fixture will execute before all module execution.
session scope : session level fixture wil execute once the automation session is initiated.
class scope :  class level fixture will execute before each test class  execution.
"""

import pytest

@pytest.fixture(scope='function', autouse=True)
def fun_setup():
    print("\n --- Initiate function fixture ---")
    yield
    print("\n --- teardown of function fixture ---")

@pytest.fixture(scope='module', autouse=True)
def module_setup():
    print("\n --- Initiate module fixture ---")
    yield
    print("\n --- teardown of module fixture ---")

@pytest.fixture(scope='package', autouse=True)
def package_setup():
    print("\n --- Initiate package fixture ---")
    yield
    print("\n --- teardown of package fixture ---")

@pytest.fixture(scope='session', autouse=True)
def session_setup():
    print("\n --- Initiate session fixture ---")
    yield
    print("\n --- teardown of session fixture ---")

def test_addition():
    num1 = 30
    num2 = 40
    assert  num1+num2 == 70

def test_multiplication():
    x = 50
    y = 7
    assert x*y == 350

def test_division(fun_setup):
    p = 60
    q = 3
    assert p//q == 5

def test_subtraction(fun_setup):
    n= 600
    m = 200
    assert n-m == 400

