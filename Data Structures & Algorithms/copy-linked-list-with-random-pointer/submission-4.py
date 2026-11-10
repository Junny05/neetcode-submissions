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
        oldToCopy = {}
        curr = head
        if not curr:
            return None
        while curr:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                oldToCopy[curr].next = oldToCopy[curr.next]
            if curr.random:
                oldToCopy[curr].random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]
         