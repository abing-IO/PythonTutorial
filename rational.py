class Rational:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        
        common = self._gcd(abs(numerator), abs(denominator))
        
        self._numerator = abs(numerator) // common
        self._denominator = abs(denominator) // common
        
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            self._numerator = -self._numerator

    @staticmethod
    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # Accessors
    def get_numerator(self):
        return self._numerator

    def get_denominator(self):
        return self._denominator

    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)
        return f"{self._numerator}/{self._denominator}"

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        new_numerator = self._numerator * other._denominator + other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        new_numerator = self._numerator * other._denominator - other._numerator * self._denominator
        new_denominator = self._denominator * other._denominator
        return Rational(new_numerator, new_denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        new_numerator = self._numerator * other._numerator
        new_denominator = self._denominator * other._denominator
        return Rational(new_numerator, new_denominator)

    def __eq__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        return self._numerator == other._numerator and self._denominator == other._denominator

    def __lt__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        return self._numerator * other._denominator < other._numerator * self._denominator

    def __gt__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if not isinstance(other, Rational):
            return NotImplemented
        return self._numerator * other._denominator > other._numerator * self._denominator

    def __repr__(self):
        return f"Rational({self._numerator}, {self._denominator})"

# Verification block
if __name__ == "__main__":
    r1 = Rational(1, 2)
    r2 = Rational(1, 3)
    r3 = Rational(2, 4) # Should reduce to 1/2
    r4 = Rational(3, 1) # Integer

    print(f"r1: {r1}")
    print(f"r2: {r2}")
    print(f"r3 (2/4): {r3}")
    print(f"r4 (3/1): {r4}")

    print(f"Numerator of r1: {r1.get_numerator()}")
    print(f"Denominator of r1: {r1.get_denominator()}")

    print(f"{r1} + {r2} = {r1 + r2}")
    print(f"{r1} - {r2} = {r1 - r2}")
    print(f"{r1} * {r2} = {r1 * r2}")

    print(f"{r1} == {r3}: {r1 == r3}")
    print(f"{r1} < {r2}: {r1 < r2}") # 1/2 < 1/3 -> False
    print(f"{r2} < {r1}: {r2 < r1}") # 1/3 < 1/2 -> True
    print(f"{r1} > {r2}: {r1 > r2}")

    # Test GCD and Sign
    r5 = Rational(-2, 4)
    print(f"Rational(-2, 4) -> {r5}")
    r6 = Rational(2, -4)
    print(f"Rational(2, -4) -> {r6}")
    r7 = Rational(-2, -4)
    print(f"Rational(-2, -4) -> {r7}")
