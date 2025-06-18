
class TestSmoke:

    def test_addition(self):
        num1 = 30
        num2 = 40
        print(f"value of num1 : {num1} and num2 : {num2}")
        assert  num1 +num2 == 70

    def test_multiplication(self):
        x = 50
        y = 7
        print(f"value of x : {x} and y : {y}")
        assert x* y == 350

    def test_division(self):
        p = 60
        q = 3
        print(f"value of p : {p} and q : {q}")
        assert p // q == 5

    def test_subtraction(self):
        n = 600
        m = 200
        assert n - m == 400

    def test_compare_values(self):
        v1 = 50
        v2 = 60
        print(f"value of v1 : {v1} and v2 : {v2}")
        assert v1 == v2
