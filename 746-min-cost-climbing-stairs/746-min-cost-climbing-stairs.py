class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(i):
            if i <=1:
                return 0
            elif i in cache:
                return cache[i]
            cache[i] = min((helper(i-1) + cost[i-1]), (helper(i-2)+cost[i-2]))
            return cache[i]
        cache = {}
        return helper(len(cost))