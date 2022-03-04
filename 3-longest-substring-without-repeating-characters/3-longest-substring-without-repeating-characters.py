class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = res =  0
        hashmap = {}
        while right < len(s):
            if s[right] not in hashmap:
                hashmap[s[right]] = 1
            else:
                hashmap[s[right]] += 1
            while hashmap[s[right]] > 1:
                left_char = s[left]
                hashmap[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            
            right += 1
        return res    