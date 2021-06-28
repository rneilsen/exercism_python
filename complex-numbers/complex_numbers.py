from math import sqrt, exp, cos, sin

class ComplexNumber:
    def __init__(self, real, imaginary):
        (self.real, self.imaginary) = (real, imaginary)

    def __eq__(self, other):
        return (self.real == other.real and self.imaginary == other.imaginary)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(
                self.real * other.real - self.imaginary * other.imaginary,
                self.real * other.imaginary + self.imaginary * other.real
        )

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        return self * other.reciprocal()

    def __abs__(self):
        return sqrt(self.real**2 + self.imaginary**2)

    def __repr__(self):
        return f"{self.real} {('+' if self.imaginary >= 0 else '-')} {abs(self.imaginary)}i"

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def reciprocal(self):
        return ComplexNumber(
                self.real / (self.real**2 + self.imaginary**2),
                - self.imaginary / (self.real**2 + self.imaginary**2)
        )

    def exp(self):
        return ComplexNumber(
                exp(self.real) * cos(self.imaginary), 
                exp(self.real) * sin(self.imaginary)
        )
