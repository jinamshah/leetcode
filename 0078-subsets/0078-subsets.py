class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def dfs(nums,path, results):
            results.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]], results)
        dfs(nums,[],results)
        return results