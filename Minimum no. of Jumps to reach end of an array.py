#User function Template for python3
class Solution:
    
	def minJumps(self, arr, n):
	    current=0   
	    farthest=0
	    jumps=0
	    for i in range(n-1):
	        
	        farthest=max(farthest, i+arr[i])    # this is the max length window possible right now i.e [i, i+1, ..farthest]
	        
	        # current makes note of last window's farthest element
	        
	        if(i==current):
	            jumps+=1
	            current=farthest # directly jump to the maximum jump found in this window ( i, i+1,...current )
	            
	            '''
	            eg. 1,1,2(a),4,2(b),0,1,1 if i = 2a, current = 2(b), in window [ 2a, 4, 2b] maximum  jump
	            is 4, so 4 will be our farthest jump
	            
	            '''
	            
	        if i==farthest and arr[i]==0:   # you reached the farthest possible element and it's a dead end
	            return -1
	    return jumps
	        
	    
	        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends


'''

For Input: 
10
2 3 1 1 2 4 2 0 1 1
It's Correct output is: 
4

Example 1:

Input:
N = 11 
arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
Output: 3 
Explanation: 
First jump from 1st element to 2nd 
element with value 3. Now, from here 
we jump to 5th element with value 9, 
and from here we will jump to the last. 
Example 2:

Input :
N = 6
arr = {1, 4, 3, 2, 6, 7}
Output: 2 
Explanation: 
First we jump from the 1st to 2nd element 
and then jump to the last element.

'''
