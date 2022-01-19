class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find_num = target
        for i in range(len(nums)):
            find_num = target - nums[i]
            try:
                second_index = nums.index(find_num)
                if i != second_index and second_index != -1:
                    return i, second_index
            except:
                continue
        return -1,-1