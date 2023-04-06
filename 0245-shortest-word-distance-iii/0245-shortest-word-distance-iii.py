class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        n = len(wordsDict)
        ans = n
        p1 = p2 = -n
        same = word1 == word2
        for i in range(n):
            if wordsDict[i] == word1:
                p1 = i
                ans = min(ans, i - p2)
                if same:
                    p2 = p1
            elif not same and wordsDict[i] == word2:
                p2 = i
                ans = min(ans, i - p1)
        return ans
        
                    