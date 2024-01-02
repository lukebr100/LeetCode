import random

# definition function randomArray
# inputs:
# size, length of array
# a, minimum value for entries
# b, maximium value for entries
# output:
# an array of length size with random entries between [a, b]
def randomArray(size, a, b):
    v = [0 for i in range(size)]
    for i in range(size):
        v[i] = random.randint(a, b)
    return v


# definition fucntion swap
# inputs:
# nums, array
# m, n integers
def swap(nums, m, n):
    L = len(nums)
    m = m % L
    n = n % L
    if m == n:
        return nums
    t = nums[m]
    nums[m] = nums[n]
    nums[n] = t
    return nums

# defintion function removeElement
# inputs: 
# nums, array
# val, value to be removed
# k, counter variable
# output:
# an array with the first k entries not equal to val
def removeElement(nums, val, k):
    L =len(nums)
    if val in nums:
        I = nums.index(val)
    else:
        return nums
    for i in range(k, L):
        if nums[i] != val:
            swap(nums, i, I)
            k = k + 1
            return removeElement(nums, val, k)
    return nums
k = 1
print(removeElement([3, 4, 1, 2, 4, 4], 4, k))

# test code
# for random arrays between size 40 and 45
# each done ten times
# the value of 7 is removed
for size in range(40, 46):
    for i in range(10):
        k = 1
        val = 7
        print(removeElement(randomArray(size, 0, 9), val, k))
