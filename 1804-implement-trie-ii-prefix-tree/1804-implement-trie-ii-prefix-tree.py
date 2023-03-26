class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.wordCount = 0
        self.startWithCount = 0
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current.startWithCount += 1
            current = current.children[char]
        current.isWord = True
        current.startWithCount += 1
        current.wordCount += 1
        return None

    def countWordsEqualTo(self, word: str) -> int:
        current = self.root
        for char in word:
            if char not in current.children: return 0
            current = current.children[char]
        return current.wordCount

    def countWordsStartingWith(self, prefix: str) -> int:
        current = self.root
        for char in prefix:
            if char not in current.children: return 0
            current = current.children[char]
        return current.startWithCount

    def erase(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children: return None
            current.startWithCount -= 1
            current = current.children[char]
        current.wordCount -=1
        current.startWithCount -= 1
        return None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)