
class Solution:
    def sort012(self,a,n):
        l=0
        m=0
        h=n-1
        while(m<=h):
            if a[m]==0:
                a[l], a[m] = a[m], a[l]
                l+=1
                m+=1
            elif a[m]==1:
                m+=1
            else:
                a[m], a[h] = a[h], a[m]
                h-=1
        return a

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends

'''

Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
Example 2:

Input: 
N = 3
arr[] = {0 1 0}
Output:
0 0 1
Explanation:
0s 1s and 2s are segregated 
into ascending order.


'''
