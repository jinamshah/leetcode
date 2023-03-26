# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def recursion(node,remainder, pathNodes,pathsList):
            if not node:
                return None
            pathNodes.append(node.val)
            
            if (remainder - node.val) == 0 and not node.left and not node.right:
                pathsList.append(list(pathNodes))
            else:
                recursion(node.left, remainder-node.val, pathNodes,pathsList)
                recursion(node.right, remainder-node.val, pathNodes,pathsList)
            pathNodes.pop()
        pathsList = []
        
        recursion(root,targetSum, [], pathsList)
        return pathsList
            
            
        
        
        