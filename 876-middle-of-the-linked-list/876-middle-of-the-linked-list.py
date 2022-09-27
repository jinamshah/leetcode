# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        storage = [head]
        while storage[-1].next:
            storage.append(storage[-1].next)
        return storage[len(storage)//2]