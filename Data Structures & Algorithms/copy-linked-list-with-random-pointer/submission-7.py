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

        copyToOld = {}
        curr = head

        if not curr:
            return None
        
        while curr:
            copyToOld[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                copyToOld[curr].next = copyToOld[curr.next]
            if curr.random:
                copyToOld[curr].random = copyToOld[curr.random]
            curr = curr.next
        
        return copyToOld[head]
