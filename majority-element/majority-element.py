class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt_dict = {}
        for num in nums:
            if num not in cnt_dict:
                cnt_dict[num] = 1
            else:
                cnt_dict[num] += 1
                if cnt_dict[num] > (len(nums)/2):
                    return num
        return list(cnt_dict.keys())[0]