class Solution:
    def get_val(s):
        if s == 'I':
            return 1
        elif s == 'V':
            return 5
        elif s == 'X':
            return 10
        elif s == 'L':
            return 50
        elif s == 'C':
            return 100
        elif s == 'D':
            return 500
        else:
            return 1000
    def romanToInt(self, s: str) -> int:
        roman_vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        s = list(s)
        total = 0
        for i in range(len(s) - 1):
            if roman_vals[s[i]] < roman_vals[s[i+1]]:
                # total -= self.get_val(s[i])
                total -= roman_vals[s[i]]
            else:
                total += roman_vals[s[i]]
        total += roman_vals[s[-1]]
        return total