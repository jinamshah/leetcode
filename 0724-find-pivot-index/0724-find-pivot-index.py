class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            if sum(nums[:index]) == sum(nums[index+1:]):
                return index
        return -1