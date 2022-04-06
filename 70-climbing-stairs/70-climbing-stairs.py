class Solution:
    def climbStairs(self, n: int) -> int:
#        Memory optimization
        if n == 1:
            return 1
        elif n == 2:
            return 2
#       Using n+1 because n starts from 1  
        second_last_step = 1
        last_step = 2
        current_step = second_last_step + last_step
        for i in range(3,n+1):
            current_step = second_last_step + last_step
            last_step, second_last_step = current_step, last_step
        return current_step
        
        # cache = [0] * n
        # return self.helper(0,n,cache)
    