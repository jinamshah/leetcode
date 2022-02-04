class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        arrLen = len(nums)
        for i in range(arrLen):
            hashmap[nums[i]] = i
        for i in range(arrLen):
            if target - nums[i] in hashmap and hashmap[target - nums[i]] != i:
                return [i, hashmap[target - nums[i]]]