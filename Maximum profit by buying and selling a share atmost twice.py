class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyone=-99999
        sellone=0
        buytwo=-99999
        selltwo=0
        for i in prices:
            buyone=max(buyone, -i)
            sellone=max(sellone, buyone+i)
            buytwo=max(buytwo, sellone-i)
            selltwo=max(selltwo, buytwo+i)
        return selltwo
