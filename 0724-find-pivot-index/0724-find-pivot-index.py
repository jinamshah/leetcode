class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr_sum = sum(nums)
        sum_of_leftside = 0
        for index, val in enumerate(nums):
            if sum_of_leftside == arr_sum - val - sum_of_leftside:
                return index
            sum_of_leftside += val
        return -1