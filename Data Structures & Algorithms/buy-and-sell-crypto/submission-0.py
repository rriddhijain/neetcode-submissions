class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b=0
        s=1
        maxprof=0
        while s<len(prices):
            if prices[b]<prices[s]:
                profit=prices[s]-prices[b]
                maxprof=max(maxprof,profit)
            else:
                b=s
            s+=1
        return maxprof
        