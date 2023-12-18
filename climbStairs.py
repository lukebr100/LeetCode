# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
                return n
        else:
            ans = 0
            if n % 2 == 0:
                ans = ans + 2
                for i in range(1, round(n / 2)):
                    ans = ans + math.comb(n - i, i)
                    print(n - i, i)
            else:
                ans = ans + 1
                for i in range(1, round(n / 2) + 1):
                    ans = ans + math.comb(n - i, i)
                    print(n - i, i)
            return ans
