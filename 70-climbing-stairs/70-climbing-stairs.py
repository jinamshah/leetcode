class Solution:
    def helper(self,i,n, cache):
        if i == n:
            return 1
        elif i > n:
            return 0
        elif cache[i] > 0:
            return cache[i]
        cache[i] = self.helper(i+1, n,cache) + self.helper(i+2,n,cache)
        return cache[i]
    def climbStairs(self, n: int) -> int:
        cache = [0] * n
        return self.helper(0,n,cache)
    