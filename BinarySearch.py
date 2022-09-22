#User function template for Python

class Solution:    
    def binarysearch(self, arr, n, k):
        l=0
        h=n-1
        while l<=h:
            mid=(l+h)//2
            if arr[mid]==k:
                return mid
            elif arr[mid]>k:
                h=mid-1
            else:
                l=mid+1
        return -1

    
'''

Example 1:

Input:
N = 5
arr[] = {1 2 3 4 5} 
K = 4
Output: 3
Explanation: 4 appears at index 3.

Example 2:

Input:
N = 5
arr[] = {11 22 33 44 55} 
K = 445
Output: -1
Explanation: 445 is not present.


'''
