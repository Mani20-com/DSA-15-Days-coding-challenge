class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        minimum=prices[0]
        profit=0
        for i in range(1,n):
            minimum=min(minimum,prices[i])
            profit=max(profit,prices[i]-minimum)


        return profit
