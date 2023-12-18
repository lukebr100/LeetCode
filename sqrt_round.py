# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

from math import floor
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            z = [0 for i in range(50)]
            z[0] = x / 2
            for i in range(1, 50):
                z[i] = z[i - 1] - (z[i - 1] * z[i - 1] - x) / (2 * z[i - 1])
            return math.floor(z[49])
