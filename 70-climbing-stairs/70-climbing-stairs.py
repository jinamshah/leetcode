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
        if n == 1:
            return 1
#       Using n+1 because n starts from 1  
        steps = [0] * (n+1)
        steps[1] = 1
        steps[2] = 2
        for i in range(3,n+1):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n]
        
        # cache = [0] * n
        # return self.helper(0,n,cache)
    