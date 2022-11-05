class Fraction:
    def __init__(self, a, b):
        self.a = a
        if b <= 0:
            raise ValueError("b cannot be equal or less than 0")
        else:
            self.b = b

    def __str__(self):
        return f"{self.a}/{self.b}"

    def __add__(self, other):
        res_a = self.a*other.b + self.b * other.a
        res_b = self.b * other.b
        return Fraction(res_a, res_b)

    def __sub__(self, other):
        res_a = self.a * other.b - self.b * other.a
        res_b = self.b * other.b
        return Fraction(res_a, res_b)

    def __mul__(self, other):
        res_a = self.a * other.a
        res_b = self.b * other.b
        return Fraction(res_a, res_b)

    def __truediv__(self, other):
        res_a = self.a * other.b
        res_b = self.b * other.a
        return Fraction(res_a, res_b)

    def __eq__(self, other):
        first_a = self.a * other.b
        second_a = other.a * self.b
        return first_a == second_a

    def __ne__(self, other):
        first_a = self.a * other.b
        second_a = other.a * self.b
        return first_a != second_a

    def __lt__(self, other):
        first_a = self.a * other.b
        second_a = other.a * self.b
        return first_a < second_a

    def __gt__(self, other):
        first_a = self.a * other.b
        second_a = other.a * self.b
        return first_a > second_a

