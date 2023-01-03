from collections import Counter

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_end, right_end = len(s), len(t)
        
        left_pointer, right_pointer = 0,0
        while left_pointer < left_end and right_pointer < right_end:
            if s[left_pointer] == t[right_pointer]:
                left_pointer += 1
            right_pointer += 1
        return left_pointer == left_end