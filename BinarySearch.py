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
