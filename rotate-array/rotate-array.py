class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        k %= length
        temp = nums[length-k:]
        x = nums[:length-k]
        x[0:0] = temp
        for i in range(len(x)):
            nums[i] = x[i]
        