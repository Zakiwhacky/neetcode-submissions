class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = -1
        r = 101
        lowest = 101
        highest = -1
        
        for i, v in enumerate(prices):
            print("curr", v, i)
            if v < lowest:
                lowest = v
                print("lowest", lowest)
            currprofit = v - lowest
            if currprofit > profit:
                profit = v - lowest
                highest = v
                print(currprofit, profit)
        #if 
        print(highest, lowest)
        
        return profit if profit > 0 else 0