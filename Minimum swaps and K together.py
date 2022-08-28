#User function Template for python3

def minSwap (arr, n, k) :
    
    # window size calculation
    c=0
    for i in arr:
        if i<=k:
            c+=1
    
    if c==0:
        return 0
            
    # window pointers        
    left,right,bad=0,0,0
    ans=9999999
    
    
    while(right<=n-1):
        # bad = no. of elements > k in current window
        if arr[right]>k:
            bad+=1
        
        # increase window size until it becomes equal to c
        if right-left+1<c:
            right+=1
            continue
        if right-left+1==c:
            ans=min(ans, bad)
            
            # move window forward
            # and decrease bad count if the leaving element on the left is > k
            if arr[left]>k:
                bad-=1
            left+=1
            right+=1
    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends


'''

Given an array arr of n positive integers and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray.

Example 1:

Input : 
arr[ ] = {2, 1, 5, 6, 3} 
K = 3
Output : 
1
Explanation:
To bring elements 2, 1, 3 together,
swap index 2 with 4 (0-based indexing),
i.e. element arr[2] = 5 with arr[4] = 3
such that final array will be- 
arr[] = {2, 1, 3, 6, 5}

Example 2:

Input : 
arr[ ] = {2, 7, 9, 5, 8, 7, 4} 
K = 6 
Output :  
2 
Explanation: 
To bring elements 2, 5, 4 together, 
swap index 0 with 2 (0-based indexing)
and index 4 with 6 (0-based indexing)
such that final array will be- 
arr[] = {9, 7, 2, 5, 4, 7, 8}

'''
