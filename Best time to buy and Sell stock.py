class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        max1=0
        max2=0
        n=len(arr)
        for i in range(1,n):
            max2+=(arr[i]-arr[i-1])
            if(max2>max1):
                max1=max2
            if(max2<0):
                max2=0
        return max1

  
'''

EXPLANATION : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39038/Kadane's-Algorithm-Since-no-one-has-mentioned-about-this-so-far-%3A)-(In-case-if-interviewer-twists-the-input)

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

'''
