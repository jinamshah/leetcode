class Solution:
    def dfs(self,wordsPresent, memo, currentWord):
        if currentWord in memo.keys():
            return memo[currentWord]
        maxLength = 1
        for i in range(len(currentWord)):
            if (currentWord[:i] + currentWord[i+1:]) in wordsPresent:
                newWord = currentWord[:i] + currentWord[i+1:]
                currentLength = 1 + self.dfs(wordsPresent, memo, newWord)
                maxLength = max(currentLength, maxLength)
                # return memo[currentWord[:i] + currentWord[i+1:]]
        memo[currentWord] = maxLength
        return maxLength
            
        
    def longestStrChain(self, words: List[str]) -> int:
        wordsPresent = set(words)
        memo = {}
        answer = 0
        for word in words:
            answer = max(self.dfs(wordsPresent,memo,word), answer)
        return answer
        # for word in words:
        #     wordsPresent[word] = 1
#         words.sort(key=(len))
#         longest_chain = 1
#         for i in range(len(words) -1):
#             if words[i] in words[i+1]:
#                 longest_chain += 1
#             else:
#                 for j in range(len(words[i+1])):
#                     # print(words[i+1][:j] + words[i+1][j+1:], words[i+1])
#                     if words[i] in (words[i+1][:j] + words[i+1][j+1:]):
#                         longest_chain += 1
#                         break
                        
#         return longest_chain
                    