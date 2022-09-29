import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        explore_stack = [(root, -math.inf, math.inf)]
        while explore_stack:
            root, lower_bound, upper_bound = explore_stack.pop()
            if not root:
                continue
            if root.val <= lower_bound or root.val >= upper_bound:
                return False
            explore_stack.append((root.right, root.val, upper_bound))
            explore_stack.append((root.left,lower_bound, root.val))
        return True