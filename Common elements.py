#User function Template for python3

class Solution:
    def commonElements (self,a, b, c, n1, n2, n3):
        ans=[]
        i,j,k=0,0,0
        while i<n1 and j<n2 and k<n3:
            if a[i]==b[j] and a[i]==c[k]:       # a[i]=b[j]=c[k]
                if not ans or ans[-1]!=a[i]:    # ans list not empty or last inserted element is 
                    ans.append(a[i])            # not equal to present element (to stop redundancy)
                i+=1
                j+=1
                k+=1
            elif a[i]<=b[j] and a[i]<=c[k]:
                i+=1
            elif b[j]<=a[i] and b[j]<=c[k]:
                j+=1
            else:
                k+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends



'''

Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?

Example 1:

Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.

'''
