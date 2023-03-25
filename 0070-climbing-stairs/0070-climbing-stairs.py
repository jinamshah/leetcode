class Solution:
    def climbStairs(self, n: int) -> int:
        # total = 0
        total = 0
        memory = [0] * (n+1)
        
        def recursive_func(i,n,memory):
            if i > n:
                return 0
            elif i == n:
                return 1
            elif memory[i] > 0:
                return memory[i]
            
            memory[i] = recursive_func(i+1,n,memory) + recursive_func(i+2,n,memory)
            return memory[i]
            
            # return recursive_func(n-1) + recursive_func(n-2)
        
        
        return recursive_func(0,n,memory)
        