# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        first = None
        prev = None
        current = head
        nextt = current.next

        index = 1

        while True: 
            if index == left: 
                first = current
                preFirst = prev 

            if left <= index and index < right: 
                temp = nextt.next

                nextt.next = current
                current.next = prev

                prev = current
                current = nextt
                nextt = temp

            elif index == right: 
                first.next = nextt

                if preFirst:
                    preFirst.next = current
                    return head
                else:
                    return current

            else: 
                prev = current
                current = nextt
                nextt = nextt.next
        

            index += 1
