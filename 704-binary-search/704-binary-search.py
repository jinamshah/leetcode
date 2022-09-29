class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high and high <= len(nums) - 1:
            print(low,high)
            if nums[low] == target:
                return low
            elif nums[high] == target:
                return high
            if nums[low] < target:
                low += 1
            if nums[high] > target:
                high -= 1
            
        return -1
        