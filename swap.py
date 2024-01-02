# define function swap of array and indices 0 < m, n < L := len(nums)
# input: array nums, index m, n
# output: nums[m, n] swapped
# eg:
# >> swap([1, 2, 3,], 0, 2)
# ans = [3, 2, 1]
# >> swap([1, 2, 3, 4], 0, 4)
# ans = [1, 2, 3, 4]
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
#print(swap([1, 2, 3, 4], 0, 4))
#print(swap([1, 2, 3], 0, 2))

#nums = [1, 2, 3, 4, 5 , 6, 7]
#for i in range(11):
    for j in range(11):
        print('If (', i, ',', j,') ==' '( i, j ),')
        print('then', swap(nums, i, j))
        nums = [1, 2, 3, 4, 5 , 6, 7]
# If ( 8 , 5 ) ==( i, j ),
# then [1, 6, 3, 4, 5, 2, 7].
# and
# If ( 5 , 8 ) ==( i, j ),
# then [1, 6, 3, 4, 5, 2, 7]. 
# 
# Therefore, we will check to see
# swap(nums, m, n) == swap(nums, n, m) for all n, m \in 0 <= m, n < L
nums = [1, 2, 3, 4, 5, 6, 7]
L = len(nums)
for i in range(L):
    for j in range(i, L):
        if i != j:
            print('If ( i, j ) ==' '(',i, ',', j,')')
            print('swap(nums, i, j) == ', swap(nums, i, j), 'and')
            nums = [1, 2, 3, 4, 5, 6, 7]
            print('If ( j, i ) ==' '(',j, ',', i,')')
            print('swap(nums, j, i) == ', swap(nums, j, i))
            nums = [1, 2, 3, 4, 5, 6, 7]
# Notice that if A = {1, 2, 3, 4, 5, 6, 7} 
# swap(A, 2, 4) for example done twice arrives
# back at A = {1, 2, 3, 4, 5, 6, 7} 
# Therefore, swap(swap(nums, i, j), i, j) == nums should be True, for all (i, j)
# Also, swap is commutative because swaping i and j is logically equivalent to swapping j and i.
# swap(nums, i, j) == swap(swap(nums, j, i)
