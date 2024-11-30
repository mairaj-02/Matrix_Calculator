# GroupB15
# Contact Person: Muhammad MAIRAJ (23098864d)

import numpy as np

class Mat2x2:
    """
    Class to represent and perform operations on a 2x2 matrix.
    Attributes:
        a, b, c, d (float): Elements of the 2x2 matrix.
    """
    def __init__(self, a, b, c, d):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.d = float(d)

    def determinant(self):
        """
        Compute the determinant of the 2x2 matrix.
        Formula: det = a * d - b * c
        """
        return self.a * self.d - self.b * self.c

    def inverse(self):
        """
        Compute the inverse of the 2x2 matrix.
        Formula:
            M^(-1) = (1/det) * [[d, -b], [-c, a]]
        Raises:
            ValueError: If the determinant is zero (singular matrix).
        """
        det = self.determinant()
        if det == 0:
            raise ValueError("Cannot invert a singular matrix.")
        return Mat2x2(self.d / det, -self.b / det, -self.c / det, self.a / det)

    def multiply(self, other):
        """
        Multiply two 2x2 matrices.
        Custom implementation without NumPy.
        """
        a1, b1, c1, d1 = self.a, self.b, self.c, self.d
        a2, b2, c2, d2 = other.a, other.b, other.c, other.d

        return Mat2x2(
            a1 * a2 + b1 * c2, a1 * b2 + b1 * d2,
            c1 * a2 + d1 * c2, c1 * b2 + d1 * d2
        )

    def power(self, n):
        """
        Compute the n-th power of the matrix using multiplication.
        Raises:
            ValueError: If n is negative (not supported).
        """
        if n < 0:
            raise ValueError("Negative powers are not supported.")
        if n == 0:
            # Return the identity matrix
            return Mat2x2(1, 0, 0, 1)

        result = self
        for _ in range(n - 1):
            result = result.multiply(self)
        return result

    def find_eigenvalues(self):
        """
        Compute eigenvalues of the matrix using NumPy.
        """
        matrix = np.array([[self.a, self.b], [self.c, self.d]])
        eigenvalues, _ = np.linalg.eig(matrix)
        return eigenvalues

    def add(self, other):
        """Add two matrices."""
        return Mat2x2(
            self.a + other.a, self.b + other.b,
            self.c + other.c, self.d + other.d
        )

    def subtract(self, other):
        """Subtract one matrix from another."""
        return Mat2x2(
            self.a - other.a, self.b - other.b,
            self.c - other.c, self.d - other.d
        )

    def divide(self, other):
        """
        Divide the matrix by multiplying with the inverse of another.
        Uses the custom inverse and multiplication methods.
        """
        inverse = other.inverse()
        return self.multiply(inverse)

    def compare(self, other):
        """
        Compare determinants of two matrices.
        Returns:
            0 if determinants are equal.
            1 if determinant of self is larger.
           -1 if determinant of self is smaller.
        """
        det_self = self.determinant()
        det_other = other.determinant()
        if det_self == det_other:
            return 0
        return 1 if det_self > det_other else -1

    def __str__(self):
        """
        Custom string representation of the matrix.
        Ensures all elements are displayed as floats with one decimal point.
        """
        return f"[[ {self.a:.1f}  {self.b:.1f}]\n [ {self.c:.1f}  {self.d:.1f}]]"

