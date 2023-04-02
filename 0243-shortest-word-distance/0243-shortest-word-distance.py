class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1Index = []
        w2Index = []
        for index,word in enumerate(wordsDict):
            if word == word1:
                w1Index.append(index)
            elif word == word2:
                w2Index.append(index)
        minDist = math.inf
        for i1 in w1Index:
            for i2 in w2Index:
                if abs(i1-i2) <= minDist:
                    minDist = abs(i1-i2)
        return minDist