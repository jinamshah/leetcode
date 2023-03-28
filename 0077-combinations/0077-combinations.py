class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        def dfs(nums,path,k,res):
            if len(path) == k:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i+1:],path+[nums[i]],k, res)
        res=[]
        dfs(nums,[],k,res)
        return res
            