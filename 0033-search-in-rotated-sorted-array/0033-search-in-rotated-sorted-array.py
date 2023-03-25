class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def getIndex(left,right):
            if nums[left] < nums[right]:
                return 0
            while right >= left:
                mid = (left+right)//2
                if nums[mid] > nums[mid+1]:
                    return mid+1
                # if nums[mid] > nums[mid-1]:
                #     return mid-1
                if nums[mid] < nums[left]:
                    right = mid-1
                else:
                    left = mid+1
        
        def search(left,right):
            while right >= left:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid
                if target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
            return -1
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        rotationPt = getIndex(0,len(nums)-1)
        if nums[rotationPt] == target:
            return rotationPt
        if rotationPt == 0:
            return search(0,len(nums)-1)
        if nums[0] > target:
            return search(rotationPt,len(nums)-1)
        return search(0,rotationPt)