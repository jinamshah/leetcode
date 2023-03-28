class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstNum = math.inf
        secondNum = math.inf
        for num in nums:
            if num <= firstNum:
                firstNum = num
            elif num <= secondNum:
                secondNum = num
            else:
                return True
        return False