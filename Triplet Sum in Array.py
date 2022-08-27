#User function Template for python3
class Solution:
    
    def find3Numbers(self,A, n, X):
        s=set()
        for i in A:
            s.add(i)
        for i in range(n-1):
            for j in range(i+1, n):
                som=X-(A[i]+A[j])
                if som in s and som!=A[i] and som!=A[j]:
                    return True
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
