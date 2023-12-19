# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Eg: If n = 3, then i) 1 + 1 + 1 = 3, ii) 1 + 2 = 3, and iii) 2 + 1 = 3. So there are three ways to climb the stairs.
import math # we need math.comb(n, k) aka n choose k or binomial coefficient 
# input: n, a positive integer, number of steps
# output: positive int, the number of ways one can climb the stairs taking 1 or 2 steps
def climbStairs(n): # define function
    if n <= 3: # first three cases coincide with number of steps
        return n
    else: # n >= 4
        ans = 0 # add to this
        if n % 2 == 0: # even number
            ans = ans + 2 # has i) 1 + 1 + ... + 1 (n-times) and ii)  2 + 2 + ... + 2 (n / 2 times), add 2 ways to running total
            for i in range(1, int(n / 2)): # w/out int(), range will not work because is.float(n / 2) == True is True
                ans = ans + math.comb(n - i, i) # I came about this formula by writing the first few cases.
                # I noticed that the ways to climb 5 steps with 1 two and 3 ones depending on placement of the two 
                # 2 + 1 + 1 + 1 = 5
                # 1 + 2 + 1 + 1 = 5
                # 1 + 1 + 2 + 1 = 5
                # 1 + 1 + 1 + 2 = 5
                # four ways, while math.comb(4, 1) == 4 is True
                # therefore, I saw that the answer to this problem is a sum of binomial coefficients
        else: # odd
            ans = ans + 1 # has i) 1 + 1 + ... + 1 but NOT 2 + 2 + ... + 2 for any number of 2's, 1 way to running total
            for i in range(1, round(n / 2) + 1): # round to zero decimals is integer, ie, is.int(round(n / 2)) == True is True
                ans = ans + math.comb(n - i, i) # same formula over differnt range
        return ans
