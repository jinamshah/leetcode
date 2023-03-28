# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = collections.deque([(root,targetSum)])
        while queue:
            current = queue.popleft()
            currentNode = current[0]
            currentTarget = current[1]
            
            if currentTarget - currentNode.val == 0 and not currentNode.left and not currentNode.right:
                return True
            if currentNode.right:
                queue.appendleft((currentNode.right, currentTarget-currentNode.val))
            if currentNode.left:
                queue.appendleft((currentNode.left, currentTarget-currentNode.val))
            
        return False