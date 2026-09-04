# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # The first node is going to be a dummy node
        new_head = ListNode()
        new_end = new_head

        while list1 != None and list2 != None:
            # Add the next value to the new list
            if list1.val < list2.val:
                val = list1.val
                list1 = list1.next
                new_end.next = ListNode(val=val)
                new_end = new_end.next
            else:
                val = list2.val
                list2 = list2.next
                new_end.next = ListNode(val=val)
                new_end = new_end.next

        while list1 != None:
            val = list1.val
            list1 = list1.next
            new_end.next = ListNode(val=val)
            new_end = new_end.next

        while list2 != None:
            val = list2.val
            list2 = list2.next
            new_end.next = ListNode(val=val)
            new_end = new_end.next

        return new_head.next



