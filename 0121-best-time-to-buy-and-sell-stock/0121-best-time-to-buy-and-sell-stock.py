class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        leastPrice = math.inf
        
        for index, price in enumerate(prices):
            if leastPrice > price:
                leastPrice = price
            elif price - leastPrice > profit:
                profit = price - leastPrice
        # print(maxPrice,leastPrice)
        return profit