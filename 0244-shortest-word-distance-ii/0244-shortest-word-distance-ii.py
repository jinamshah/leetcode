class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordOccurrences = {}
        for index, word in enumerate(wordsDict):
            if word not in self.wordOccurrences:
                self.wordOccurrences[word] = [index]
            else:
                self.wordOccurrences[word].append(index)
        

    def shortest(self, word1: str, word2: str) -> int:
        if word1 not in self.wordOccurrences or word2 not in self.wordOccurrences:
            return None
        w1Indices = self.wordOccurrences[word1]
        w2Indices = self.wordOccurrences[word2]
        minDist = math.inf
        for i1 in w1Indices:
            for i2 in w2Indices:
                minDist = min(minDist, abs(i1-i2))
        return minDist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)