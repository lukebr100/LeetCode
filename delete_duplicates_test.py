from delete_duplicates import delete_duplicates
import random

nums0 = [1, 2, 3, 4, 5]
print(delete_duplicates(nums0), 'nums0')

nums1 = [1, 2, 2, 3, 3, 3, 4, 4]
print(delete_duplicates(nums1), 'nums1')

nums2 = [1]
print(delete_duplicates(nums2), 'nums2')

nums3 = [1, 2, 3, 4, 5, 5, 5, 5, 5]
print(delete_duplicates(nums3), 'nums3')


x = sorted([random.randrange(100) for i in range(100)])
print(x, 'before delete duplicates')

print(delete_duplicates(x), 'after delete duplicates')
