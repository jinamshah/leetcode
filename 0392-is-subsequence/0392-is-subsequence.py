from collections import Counter

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_end, right_end = len(s), len(t)
        
        def recursive(left_index, right_index):
            if left_index == left_end:
                return True
            elif right_index == right_end:
                return False
            if s[left_index] == t[right_index]:
                left_index += 1
            right_index += 1
            return recursive(left_index,right_index)
        return recursive(0,0)