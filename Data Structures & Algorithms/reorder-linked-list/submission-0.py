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

        
        offset = length - 1
        n = head

        while offset >= 2:
            following = n.next

            t = n
            for i in range(offset):
                t = t.next

            n.next = t
            n.next.next = following
            n = n.next.next
            offset-=2

        if offset == 1:
            n = n.next
        n.next = None

        return