class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentVal = maxVal = nums[0]
        for num in nums[1:]:
            currentVal = max(num, currentVal + num)
            maxVal = max(maxVal, currentVal)
        return maxVal