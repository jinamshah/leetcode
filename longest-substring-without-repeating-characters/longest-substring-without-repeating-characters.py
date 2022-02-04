class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strLen = len(s)
        answers = []
        if strLen > 0:
            for i in range(strLen):
                answer = 1
                seen = []
                seen.append(s[i])
                for j in range(i+1,strLen):
                    if s[j] not in seen:
                        seen.append(s[j])
                        answer += 1
                    else:
                        break
                answers.append(answer)
            return max(answers)
        else:
            return 0