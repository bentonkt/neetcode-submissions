# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find the length of the list
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        # Find index of the node to be removed
        index = length - n
        if index == 0:
            return head.next

        pointer = head
        while index > 1: # Stop right before the node to be removed
            pointer = pointer.next
            index -= 1
            

        pointer.next = pointer.next.next

        return head