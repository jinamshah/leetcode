class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(candidates,path,res,target):
            if target < 0: return
            if target == 0:
                res.append(path)
                return
            for i in range(len(candidates)):
                dfs(candidates[i:],path+[candidates[i]],res, target-candidates[i])
                
        candidates.sort()
        res = []
        dfs(candidates,[],res,target)
        return res