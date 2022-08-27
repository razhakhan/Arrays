
def sol(nums):
  return [i for i in set(nums) if nums.count(i) > len(nums)//3]

'''

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

'''
