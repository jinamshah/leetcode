class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_characters = []
        final_substrings = []
        if len(s) > 0:
            for i in range(len(s)):
                current_characters = [s[i]]
                # print(i, len(s))
                for j in range(i+1, len(s)):
                    # print(j)
                    if s[j] in current_characters:
                        break
                    else:
                        current_characters.append(s[j])
                    # print(current_characters)
                final_substrings.append(current_characters)
            final_substrings = sorted(final_substrings, key=len, reverse=True)
            # print(final_substrings)
            return len(final_substrings[0])
        else:
            return 0