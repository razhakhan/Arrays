#User function Template for python3

def pendulumArrangement(arr, n):
    ans=[0]*n
    arr.sort()
    start=end=mid=(n-1)//2
    ans[mid]=arr[0]
    
    for i in range(1, n):
        if i%2==0:
            start-=1
            ans[start]=arr[i]
        else:
            end+=1
            ans[end]=arr[i]
    
    return ans
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        answer = pendulumArrangement(arr, n)
        print(*answer)

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends

'''

Example 1:
Input : 
n = 5
arr[] = {1, 3, 2, 5, 4}
Output :
5 3 1 2 4
Explanation: 
The minimum element is 1, so it is 
moved to the middle. The next higher
element 2  is moved to the right of 
the middle element while the next 
higher element 3 is moved to the left 
of the middle element and this process
is continued.

Example 2:
Input :
n = 5 
arr[] = {11, 12, 31, 14, 5}
Output :
31 12 5 11 14

'''
