import re
class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        edgeCases = {
            "IV": "IIII",
            "IX": "VIIII",
            "XL": "XXXX",
            "XC":"LXXXX",
            "CD": "CCCC",
            "CM": "DCCCC"
        }
        answer = 0
        for key,val in edgeCases.items():
            s = s.replace(key,val)
        for char in s:
            answer += romanDict[char]
        return answer
            
            