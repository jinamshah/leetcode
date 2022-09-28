"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Recursion:
# answer_array = []
# def recursion(root_node):
#     if not root_node:
#         return None
#     if not root_node.children:
#         answer_array.append(root_node.val)
#         return None
#     else:
#         answer_array.append(root_node.val)
#         for child in root_node.children:
#             recursion(child)
# recursion(root)
# return answer_array

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        answer_array = []
        explore_stack = [root]
        current_node = root
        while explore_stack:
            current_root = explore_stack.pop()
            answer_array.append(current_root.val)
            if current_root.children:
                current_root.children.reverse() # for left to right popping
                for child in current_root.children:
                    explore_stack.append(child)
        
        return answer_array