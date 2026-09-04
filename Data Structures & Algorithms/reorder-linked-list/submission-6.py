# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        cur = head
        nodes.append(cur)
        while cur.next: 
            cur = cur.next
            nodes.append(cur)

        
        

        left = 0
        right = len(nodes) - 1


        while left < right: 
            print(right)
            print(left)
            if left != 0: 
                temp.next = nodes[left]

            nodes[left].next = nodes[right]
            temp = nodes[right]

            left += 1
            right -= 1
    

        if left == right and left != 0: 
            temp.next = nodes[left]
            temp = temp.next


        if left != 0: 
            temp.next = None

        

