import itertools

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums) - 1):
            left_pointer, right_pointer = i+1, len(nums) -1
            while left_pointer < right_pointer:
                summation = nums[i] + nums[left_pointer] + nums[right_pointer]
                if summation > target:
                    right_pointer -= 1
                elif summation < target:
                    left_pointer += 1
                else:
                    return summation
                ans = min(ans, summation, key=lambda x: abs(target-x))
        return ans
            