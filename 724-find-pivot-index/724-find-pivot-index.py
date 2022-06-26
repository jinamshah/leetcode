class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
        # for i in range(0, len(nums)):
        #     # print(nums[0:i], nums[i+1:len(nums)])
        #     left_sum = sum(nums[0:i])
        #     right_sum = sum(nums[i+1:len(nums)])
        #     if left_sum == right_sum:
        #         return i
        #     # print(left_sum, right_sum)
        # return -1