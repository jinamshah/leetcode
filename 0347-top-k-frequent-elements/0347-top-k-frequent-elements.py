class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == nums:
            return nums
        counts = Counter(nums)
        # heapq.heapify(counts)
        # print(counts)
        buckets = defaultdict(list)
        for num,count in counts.items():
            if count in buckets.keys():
                buckets[count].append(num)
            else:
                buckets[count] = [num]
        buckets = sorted(buckets.items(),reverse=True)
        # for 
        answers = []
        for key, val in buckets:
            if k == 0:
                break
            if k >= len(val):
                answers.extend(val)
                k -= len(val)
            else:
                answers.extend(val[:k+1])
                k = 0
        
        # return heapq.nlargest(k, counts.keys(), key=counts.get)
        return answers
        