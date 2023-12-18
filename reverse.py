# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
class Solution:
    def reverse(self, x: int) -> int:
        sign = 0
        if x < 0:
            sign = -1
            x = -1 * x
        elif x > 0:
            sign = 1
        x = str(x)
        x = x[::-1]
        x = int(x)
        x = sign * x
        if x >= -2**31 and x <= 2**31 - 1:
            return x
        else: 
            return 0
