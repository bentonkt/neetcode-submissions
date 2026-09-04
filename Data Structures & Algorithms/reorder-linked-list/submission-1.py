# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find length of the list
        if not head:
            return None
        length = 0
        finder = head
        while finder: 
            finder = finder.next
            length += 1

        
        # Reverse the second half of the list
        # First, get to the starting node of the second half
        mid = math.ceil(length / 2)

        pointer = head
        for i in range(mid - 1):
            pointer = pointer.next
        
        # Pointer is at the node before the middle node, so we should start reversing
        # We're going to update pointer to point at the new middle node after the reversing
        cur = pointer.next
        prev = None
        while cur != None:
            next_one = cur.next
            cur.next = prev

            prev = cur
            cur = next_one

        pointer.next = prev
        pointer = pointer.next # Now, pointer is in the second half of the array, which has been reversed

        l = head
        for i in range(mid - 1):
            lnext = l.next
            l.next = pointer
            rnext = pointer.next
            pointer.next = lnext
            l = lnext
            pointer = rnext

        if length % 2 == 0:
            l.next = pointer
            l = l.next
        l.next = None



        return