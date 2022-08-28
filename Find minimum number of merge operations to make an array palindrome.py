# Python program to find number of operations
# to make an array palindrome

# Returns minimum number of count operations
# required to make arr[] palindrome
def findMinOps(arr, n):
	ans = 0 # Initialize result

	# Start from two corners
	i,j = 0,n-1
	while i<=j:
		# If corner elements are same,
		# problem reduces arr[i+1..j-1]
		if arr[i] == arr[j]:
			i += 1
			j -= 1

		# If left element is greater, then
		# we merge right two elements
		elif arr[i] > arr[j]:
			# need to merge from tail.
			j -= 1
			arr[j] += arr[j+1]
			ans += 1

		# Else we merge left two elements
		else:
			i += 1
			arr[i] += arr[i-1]
			ans += 1

	return ans


# Driver program to test above
arr = [1, 4, 5, 9, 1]
n = len(arr)
print("Count of minimum operations is " + str(findMinOps(arr, n)))

'''

Example : 

Input : arr[] = {15, 4, 15}
Output : 0
Array is already a palindrome. So we
do not need any merge operation.

Input : arr[] = {1, 4, 5, 1}
Output : 1
We can make given array palindrome with
minimum one merging (merging 4 and 5 to
make 9)

Input : arr[] = {11, 14, 15, 99}
Output : 3
We need to merge all elements to make
a palindrome.

'''
