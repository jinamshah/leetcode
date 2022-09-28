# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        explore_array = [root]
        current_level = 0
        answer_array = []
        while explore_array:
            answer_array.append([])
            # root = explore_queue.pop(0)
            # length = len(queue)
            for i in range(len(explore_array)):
                root = explore_array.pop(0)
                answer_array[current_level].append(root.val)
                
                if root.left:
                    explore_array.append(root.left)
                if root.right:
                    explore_array.append(root.right)
            current_level += 1
        return answer_array
            