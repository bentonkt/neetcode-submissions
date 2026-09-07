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
        curOld = head
        nodeMap = {}
        res = Node(0)
        prev = res
        curNew = None
        while curOld:
            curNew = Node(curOld.val)
            prev.next = curNew

            nodeMap[curOld] = curNew

            prev = curNew
            curOld = curOld.next
            curNew = curNew.next

        # Now random pointers
        curNew = res.next
        curOld = head
        while curOld: 
            oldRandom = curOld.random
            if not oldRandom:
                newRandom = None
            else:
                newRandom = nodeMap[oldRandom]
            curNew.random = newRandom

            curOld = curOld.next
            curNew = curNew.next

        return res.next

        


