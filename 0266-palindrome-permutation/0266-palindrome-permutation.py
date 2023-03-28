import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        hashmap = collections.Counter(s)
        if len(s) % 2 == 0:
            for k, v in hashmap.items():
                if v % 2 != 0:
                    return False
            return True
        else:
            answer = False
            for k,v in hashmap.items():
                if v % 2 != 0:
                    if not answer:
                        answer = True
                    else:
                        return False
            return answer