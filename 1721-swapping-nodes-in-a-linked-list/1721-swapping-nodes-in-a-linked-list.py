# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        allElements = []
        k -= 1
        tempHead = head
        while tempHead.next:
            allElements.append(tempHead)
            tempHead = tempHead.next
        allElements.append(tempHead)
        
        allElements[k].val, allElements[len(allElements) - k - 1].val = allElements[len(allElements) - k - 1].val, allElements[k].val
        return head
        
        