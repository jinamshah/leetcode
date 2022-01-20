# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals = []
        def internal_func(root,k):
            if not root:
                return False
            if root.val in vals:
                # ans = True
                return True
            else:
                vals.append(k-root.val)
                # vals[k-root.val] = True
                # internal_func(root.left, k)
                # internal_func(root.right, k)
                return internal_func(root.left, k) or internal_func(root.right, k)
            # return ans
        
        return internal_func(root,k)