class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        num_0 = 0
        num_1 = 1
        num_2 = 1
        for n in range(3,n+1):
            temp_num = num_0+num_1+num_2
            num_0 = num_1
            num_1 = num_2
            num_2 = temp_num
            
        return num_2