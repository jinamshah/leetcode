class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0
        hashtable = collections.Counter(s)
        hashtable = {k:v for k,v in sorted(hashtable.items(), key=lambda x: x[1], reverse=True)}
        for char,val in hashtable.items():
            answer += val//2 * 2
            if answer % 2 == 0 and val % 2 == 1:
                answer += 1
        return answer
                