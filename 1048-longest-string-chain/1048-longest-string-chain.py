class Solution:
#   Bottom-Up Approach  (Slower, more storage)
#     def longestStrChain(self, words: List[str]) -> int:
        # words.sort(key=len)
        # sequenceDict = dict.fromkeys(words,0)
        # longestWordSequenceLength = 1
        # for i in range(len(words)):
        #     presentLength = 1
        #     currentWord = words[i]
        #     for j in range(len(currentWord)):
        #         subWord = currentWord[:j] + currentWord[j+1:]
        #         if subWord in words:
        #             presentLength = max(presentLength, sequenceDict[subWord] + 1)
        #     sequenceDict[currentWord] = presentLength
        #     longestWordSequenceLength = max(presentLength,longestWordSequenceLength)
        # return longestWordSequenceLength
#   Depth First Search Approach (Faster, less storage)
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
                    