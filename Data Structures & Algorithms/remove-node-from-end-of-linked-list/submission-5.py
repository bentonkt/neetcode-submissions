# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1

        print(length)

        index = length - n + 1
        if index == 1:
            return head.next
        print(index)

        prev = head
        cur = head.next if head else None
        for i in range(index - 2):
            prev = cur
            cur = cur.next

        prev.next = cur.next if cur else None

        return head

