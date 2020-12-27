# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    for k in range(len(prices)-1,0,-1):
        if(min(prices[0:k]) < prices[k]):
            max_profit = max(max_profit,prices[k] - min(prices[0:k]))
    return max_profit