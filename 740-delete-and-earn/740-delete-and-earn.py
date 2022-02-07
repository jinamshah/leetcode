class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        prev = None
        avoid = using = 0
        for k in sorted(count):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * count[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * count[k] + avoid
            prev = k
        return max(avoid, using)
#         nums.sort(reverse=True)
#         points_hashmap = {}
#         for iterator1 in range(len(nums)):
#             temp_nums = list(filter(lambda a: a not in points_hashmap.keys(), nums))
#             if nums[iterator1] not in points_hashmap.keys():
#                 points = sum(list(filter(lambda a: a == nums[iterator1], nums)))
#                 # for iterator2 in range(len(nums)):
#                 #     if abs(nums[iterator1] - nums[iterator2]) == 1:
#                 #         points += nums[iterator2]
#                 x = list(filter(lambda a: a not in [nums[iterator1]-1, nums[iterator1], nums[iterator1]+1], temp_nums))
#                 points_hashmap[nums[iterator1]] = points + sum(x)
        
        
#         points_hashmap = dict(sorted(points_hashmap.items(), key= lambda x: x[1], reverse=True))
#         print(points_hashmap)
#         total_points = 0
#         temp_nums = nums
#         for number, greedy_value in points_hashmap.items():
#             # print(number, temp_nums)
#             if temp_nums:
#                 if number in temp_nums:
#                     total_points += sum(list(filter(lambda a: a == number, temp_nums)))
#                     temp_nums = list(filter(lambda a: a not in [number, number-1, number+1], temp_nums))
#             else:
#                 break
            
#         return total_points   
        