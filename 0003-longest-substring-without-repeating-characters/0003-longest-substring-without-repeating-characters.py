class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        chars = {}
        left,right = 0,0
        answer = 0
        for right in range(len(s)):
            right_char = s[right]
            if right_char in chars.keys():
                left = max(left,chars[right_char])
            answer = max(answer, right-left+1)
            chars[right_char] = right+1
            # right += 1
        return answer