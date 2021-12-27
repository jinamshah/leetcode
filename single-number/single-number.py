class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt_dict = {}
        for num in nums:
            if num not in cnt_dict:
                cnt_dict[num] = 1
            else:
                del cnt_dict[num] 
        return list(cnt_dict.keys())[0]
        