class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        target = 0
        for index, num in enumerate(nums):
            hashmap = {}
            internal_nums = nums[:index] + nums[index+1:]
            left = 0
            right = len(internal_nums)-1
            while left < right:
                summation = internal_nums[left] + internal_nums[right]
                if summation + num == target:
                    op = [internal_nums[left], num, internal_nums[right]]
                    op.sort()
                    output.append(op)
                    left += 1
                    right -= 1
                elif summation + num < target:
                    left += 1
                else:
                    right -=1
                # print(left,right, internal_nums)
        return set(tuple(row) for row in output)