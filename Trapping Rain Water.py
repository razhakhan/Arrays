'''
logic :

Follow the steps mentioned below to implement the idea:

Take two pointers l and r. Initialize l to the starting index 0 and r to the last index N-1.
Since l is the first element, left_max would be 0, and right_max for r would be 0.
While l ≤ r, iterate the array. We have two possible conditions
Condition1 : left_max <= right max
Consider Element at index l
Since we have traversed all elements to the left of l, left_max is known 
For the right max of l, We can say that the right max would  always be >= current r_max here
So, min(left_max,right_max) would always equal to left_max in this case
Increment l.
Condition2 : left_max > right max
Consider Element at index r
Since we have traversed all elements to the right of r, right_max is known
For the left max of l, We can say that the left max would  always be >= current l_max here
So, min(left_max,right_max) would always equal to right_max in this case
Decrement r.


'''





class Solution:
    def trappingWater(self, arr,n):
        l=0
        r=n-1
        lmax=0
        rmax=0
        res=0
        while(l<=r):
            if rmax<=lmax:
                res+=max(0, rmax-arr[r])
                rmax=max(rmax, arr[r])
                r-=1
            else:
                res+=max(0, lmax-arr[l])
                lmax=max(lmax, arr[l])
                l+=1
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends

'''

Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
 

Example 1:

Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output:
10
Explanation: 

Example 2:

Input:
N = 4
arr[] = {7,4,0,9}
Output:
10
Explanation:
Water trapped by above 
block of height 4 is 3 units and above 
block of height 0 is 7 units. So, the 
total unit of water trapped is 10 units.

'''
