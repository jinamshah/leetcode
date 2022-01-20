import itertools
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = length - 1
            while left < right:
                summation = nums[i] + nums[left] + nums[right]
                if summation > 0:
                    right -= 1
                elif summation < 0:
                    left += 1
                
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans
                    