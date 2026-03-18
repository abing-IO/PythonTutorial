class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def reduce(self):
        g = self.gcd(self.numerator, self.denominator)
        self.numerator //= g
        self.denominator //= g

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)

    def __sub__(self, other):
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Rational(num, den)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Rational(num, den)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator


r1 = Rational(2, 4)
r2 = Rational(3, 5)

print("r1 =", r1)
print("r2 =", r2)

print("Addition:", r1 + r2)
print("Subtraction:", r1 - r2)
print("Multiplication:", r1 * r2)

print("r1 == r2:", r1 == r2)
print("r1 < r2:", r1 < r2)
print("r1 > r2:", r1 > r2)