# input: list of numbers with n elements
# output: list of k <= n unique elements

def delete_duplicates(nums):
    nums = sorted(nums) # sorts the list in non-decreasing order
    n = len(nums) # store length of list nums into variable n
    i = 0 # initalize i
    while i < n - 1: # start while loop, proceed until i is second to last entry of nums
        if nums[i] == nums[i+1]: # check condition: if the ith spot of nums is equal to the next entry (a duplicate entry)
            nums = nums[0:i+1] + nums[i+2:n+1] # then into nums, store a slicing of nums that excludes the (i+1)st entry
            n = len(nums) # recalculate length of nums b/c nums length decreased by one 
        else:   # if not duplicate entries at i and (i+1)
            i = i + 1 # then add to counter
    return nums
