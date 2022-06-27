class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        num_0 = 0
        num_1 = 1
        num_2 = 1
        for n in range(n-2):
            num_0,num_1,num_2 = num_1,num_2, num_1+num_2+num_0
        return num_2