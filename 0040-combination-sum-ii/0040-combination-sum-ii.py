class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(candidates,path,res,target):
            if target < 0:
                return
            elif target == 0:
                if path not in res:
                    res.append(path)
                return
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                dfs(candidates[i+1:], path+[candidates[i]], res, target-candidates[i])
                
        res = []
        candidates.sort()
        dfs(candidates, [],res,target)
        return res