#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        arr=sorted(arr)
        ans=arr[n-1]-arr[0]
        for i in range(1, n):
            if arr[i]-k<0:
                continue
            tempmin=min(arr[0]+k, arr[i]-k)
            tempmax=max(arr[i-1]+k, arr[n-1]-k)
            ans=min(ans, tempmax-tempmin)
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends

'''

Example 1:

Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as 
{3, 3, 6, 8}. The difference between 
the largest and the smallest is 8-3 = 5.
Example 2:

Input:
K = 3, N = 5
Arr[] = {3, 9, 12, 16, 20}
Output:
11
Explanation:
The array can be modified as
{6, 12, 9, 13, 17}. The difference between 
the largest and the smallest is 17-6 = 11.

'''
