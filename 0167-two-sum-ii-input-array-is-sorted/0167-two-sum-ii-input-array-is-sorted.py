class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        left = 0
        right = len(numbers)-1
        while left < right:
            summation = numbers[left] + numbers[right]
            if summation == target:
                return [left+1, right+1]
            elif summation < target:
                left += 1
            else:
                right -= 1
        return -1