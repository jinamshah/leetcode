# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals = []
        ans = False
        def internal_func(root,k):
            nonlocal ans
            if not root:
                return False
            if root.val in vals:
                # print(root.val,k,vals)
                ans = True
                # return True
            # elif root.val > k:
            #     print(root.val,k,self.vals)
            #     return False
            else:
                vals.append(k-root.val)
                # print(root.val,k,vals)
                # findTarget(root.left, k-root.val)
                # findTarget(root.right, k-root.val)
                # internal_func(root.left, k-root.val)
                internal_func(root.left, k)
                internal_func(root.right, k)
            # return ans
        internal_func(root,k)
        return ans