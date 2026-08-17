class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = 101  
        for i, v in enumerate(prices):
            if v < lowest:
                lowest = v
            currprofit = v - lowest
            if currprofit > profit:
                profit = v - lowest
        return profit if profit > 0 else 0