"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer_array = []
        def recursion(root_node):
            if not root_node:
                return None
            if not root_node.children:
                answer_array.append(root_node.val)
                return None
            else:
                answer_array.append(root_node.val)
                for child in root_node.children:
                    recursion(child)
        recursion(root)
        return answer_array
        