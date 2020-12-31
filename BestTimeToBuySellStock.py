# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

#=================Solution=====================
# Easy peasy, passed on Leetcode:
# Essentially DP
# There's actually a neater way to do this, only keeping track of the price and not the buy/sell values

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Goal is to find max difference such that max index > min index
        # We can do this by traversing the array and holding a min variable, representing the best time to buy
        if not prices:
            return 0
        buyPrice = sellPrice = prices[0]
        maxProfit = 0
        for price in prices:
            if price < buyPrice:
            elif price - buyPrice > maxProfit:
                maxProfit = price - buyPrice
            
            if price > sellPrice:
                sellPrice = price
            if price < buyPrice:
                buyPrice = sellPrice = price
            maxProfit = max(maxProfit, sellPrice - buyPrice)
        return maxProfit
        
