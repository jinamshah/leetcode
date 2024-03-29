import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = math.inf
        maxprofit = 0
        for i in range(0,len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif (prices[i] - minprice) > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit