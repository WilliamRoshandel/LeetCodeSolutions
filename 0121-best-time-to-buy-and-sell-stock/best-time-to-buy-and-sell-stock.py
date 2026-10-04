class Solution(object):
    def maxProfit(self, prices):
        
        maxProfit = 0
        lowest = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            elif prices[i] - lowest > maxProfit:
                maxProfit = prices[i] - lowest

        return maxProfit

            