class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        for index, char in enumerate(s):
            if char in hashmap.keys():
                if hashmap[char] != t[index]:
                    return False
                else:
                    continue
            elif t[index] in hashmap.values():
                return False
            else:
                hashmap[char] = t[index]
        return True