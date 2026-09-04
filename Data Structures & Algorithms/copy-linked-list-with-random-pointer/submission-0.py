"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Use hashmap to map old nodes to new nodes
        d = { None: None}
        # On the first pass, simply initialize the copied nodes with the values
        cur = head
        while cur:
            copy = Node(x=0)
            d[cur] = copy
            cur = cur.next

        # Second pass, assign the pointers
        cur = head
        while cur:
            copy = d[cur]
            copy.next = d[cur.next]
            copy.random = d[cur.random]
            copy.val = cur.val
            cur = cur.next

        return d[head]
        