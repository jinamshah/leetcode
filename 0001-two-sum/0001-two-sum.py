class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if num in hashmap.keys():
                return [i,hashmap[num]]
            hashmap[target-num] = i
        return -1