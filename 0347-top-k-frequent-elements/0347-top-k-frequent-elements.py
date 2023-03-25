class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == nums:
            return nums
        nums.sort()
        counts = Counter(nums)
        # heapq.heapify(counts)
        # print(counts)
        return heapq.nlargest(k, counts.keys(), key=counts.get)
        