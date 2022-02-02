
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_char_dict = {}
        for char in set(s):
            s_char_dict[char] = s.count(char)
        
        t_char_dict = {}
        for char in set(t):
            t_char_dict[char] = t.count(char)
            
        if s_char_dict == t_char_dict: return 0
        
        answer = 0
        for char in t_char_dict.keys():
            if char not in s_char_dict.keys():
                answer += t_char_dict[char]
        total_leeway = answer
        for char in s_char_dict.keys():
            if char not in t_char_dict.keys():
                total_leeway -= s_char_dict[char]
            else:
                total_leeway -= abs(s_char_dict[char] - t_char_dict[char])
        # print(answer, total_leeway)   
#         dividing total_leeway by 2 because each operation is an interchange and not a "removal and addition" of characters
        answer += abs(total_leeway//2)
        return answer
        