class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        if target in nums:
            while low<=high:
                mid = (low + high)//2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        else:
            while low<high:
                mid = (low + high)//2
                if target > nums[mid]:
                    if mid + 1 < high and target < nums[mid+1]:
                        return mid + 1
                    low = mid + 1
                else:
                    high = mid
            return high
                
            
        