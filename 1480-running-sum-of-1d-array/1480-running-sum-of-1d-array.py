class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            if len(answer) > 0:
                answer.append(answer[-1] + num)
            else:
                answer.append(num)
        return answer