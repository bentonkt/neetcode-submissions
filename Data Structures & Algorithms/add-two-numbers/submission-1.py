# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        resPointer = res
        p1 = l1
        p2 = l2
        carry = 0
        while p1 and p2: 
            add = p1.val + p2.val

            if carry: 
                add += 1
                carry = 0

            if add // 10: 
                carry = 1
                add = add % 10

            newNode = ListNode(add)
            resPointer.next = newNode
            resPointer = newNode

            p1 = p1.next
            p2 = p2.next

        while p1: 
            add = p1.val

            if carry: 
                add += 1
                carry = 0
            if add // 10: 
                carry = 1
                add = add % 10


            newNode = ListNode(add)
            resPointer.next = newNode
            resPointer = newNode

            p1 = p1.next
            
        while p2: 
            add = p2.val

            if carry: 
                add += 1
                carry = 0
            if add // 10: 
                carry = 1
                add = add % 10


            newNode = ListNode(add)
            resPointer.next = newNode
            resPointer = newNode

            p2 = p2.next
        
        if carry: 
            resPointer.next = ListNode(1)

        return res.next
