# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[1]
        
        prev = ListNode()
        res = prev
        while True:
            # Keep track of the lowest value across all the lists
            min_head = lists[0]
            index = 0
            for i, head in enumerate(lists):
                if head == None:
                    continue

                if not min_head or head.val < min_head.val:
                    min_head = head
                    index = i
                
            prev.next = min_head
            prev = prev.next
            if min_head == None:
                break
            lists[index] = lists[index].next
        
        return res.next