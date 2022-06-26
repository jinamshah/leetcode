class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum = nums[0]
        final_output = [nums[0]]
        for i in range(1,len(nums)):
            current_sum += nums[i]
            final_output.append(current_sum)
        return final_output