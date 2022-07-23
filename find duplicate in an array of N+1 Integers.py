class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            x=nums[i]%n         # use the nums array as a hash table
            nums[x]=nums[x]+n   # eg. index 2 stores the count of element '2'
                                # eg. nums before =[1,3,4,2,2], nums after =[1, 8, 14 ,7, 7]
                                #                                            0  1   2  3  4
        for i in range(n):
            if(nums[i]>=n*2):   # repeated element will have n added 2 times, so it'll be greater than n%2
                return i
                
 '''
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
  
 '''
