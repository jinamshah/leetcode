class Solution:
    def fib(self, n: int) -> int:
        first_num = 0
        second_num = 1
        if n == 0 or n == 1:
            return n
        for i in range (2,n+1):
            first_num, second_num = second_num, (first_num+second_num)
        return second_num