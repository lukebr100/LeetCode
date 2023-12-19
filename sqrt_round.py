# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# input: an integer
# output: the square root rounded down to nearest integer

# the idea is to obtain a number close to the postive zero of the function f(x) = x^2 - c
# by finding the zero of the tangent line.
# this requires a 'good' intial guess of the zero, I use x / 2 as the intial guess.
# a better intial guess may enable a faster convergence, and thus less iterations required in the for loop

from math import floor
def mySqrt(x):
    if x == 0: # otherwise, the code included in else would divide by zero
        return 0
    else:
        z = [0 for i in range(50)] # initalize a vector where the sequential approximations are stored
        z[0] = x / 2 # intial guess goes in first slot
        for i in range(1, 50): # 49 iterations
            z[i] = z[i - 1] - (z[i - 1] * z[i - 1] - x) / (2 * z[i - 1]) 
            # x_{n + 1} = x_n - f(x_n) / f'(x_n), x_{n + 1} is the next approximation. it is in terms of the previous approx, x_n
            # this formula is gotten by setting the equation of the tangent line
        return math.floor(z[49]) # round down the last approximation
        # error could occur if z[49] is close to sqrt(x) but less than floor(srrt(x))
