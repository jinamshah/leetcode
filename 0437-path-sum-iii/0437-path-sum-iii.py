# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        numPaths = 0
        hashmap = defaultdict(int)
        
        def recursion(currentNode,  prefixSum):
            nonlocal numPaths
            if not currentNode:
                return
            prefixSum += currentNode.val
            
            if prefixSum == targetSum:
                numPaths += 1
            numPaths += hashmap[prefixSum-targetSum]
            hashmap[prefixSum] += 1
            if currentNode.left:
                recursion(currentNode.left, prefixSum)
            if currentNode.right:
                recursion(currentNode.right, prefixSum)
            hashmap[prefixSum] -= 1
            
        recursion(root,0)
        return numPaths
            