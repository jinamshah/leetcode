# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
            if arr[-1].next in arr:
                return arr[-1].next
        return None