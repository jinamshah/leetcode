class Solution:
    def removeVowels(self, s: str) -> str:
        op = ''
        for char in s:
            if char not in ['a','e','i','o','u']:
                op+= char
        return op