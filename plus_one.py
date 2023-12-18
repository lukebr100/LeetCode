# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        L = len(digits)
        dig = 0
        for i in range(1, L + 1):
            dig = dig + digits[-i] * 10**(i - 1)
        dig = dig + 1
        dig = str(dig)
        K = len(dig)
        ans = [0 for i in range(K)]
        for i in range(1, K + 1):
            ans[-i] = int(dig[-i])
        return ans
