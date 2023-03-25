class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)
        right_index = len(nums)-2
        for index in range(1, len(nums)):
            left_prod[index] = left_prod[index-1] * nums[index-1]
            right_prod[right_index] = right_prod[right_index+1] * nums[right_index+1]
            right_index -=1
        return [l*r for l,r in zip(left_prod,right_prod)]
        
        