# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get a pointer at the middle
        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        print(slow.val)
        # Now, reverse the second half of the list
        second = slow.next
        prev = None
        slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        mid = prev

        # Now, merge from head and slow
        first = head
        while mid and first:
            print(1)
            tmp1 = first.next
            tmp2 = mid.next
            first.next = mid
            mid.next = tmp1

            first = tmp1
            mid = tmp2

