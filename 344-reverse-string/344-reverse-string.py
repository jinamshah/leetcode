class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper_func(left_pointer, right_pointer):
            if left_pointer < right_pointer:
                s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]  # This needs to be done at the same time to use both values
                helper_func(left_pointer + 1, right_pointer - 1)
        helper_func(0, len(s)-1)
        