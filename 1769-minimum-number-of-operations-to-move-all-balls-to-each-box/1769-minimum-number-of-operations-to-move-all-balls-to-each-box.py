class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        hashmap = {}
        for index in range(len(boxes)):
            hashmap[index] = int(boxes[index])
        answers = [0] * len(boxes)
        for key, val in hashmap.items():
            answers[key] = sum([v*abs(k-key) for k,v in hashmap.items() if k!=key])
        return answers