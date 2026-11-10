# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummyNode = ListNode(0, head)
        
        groupPrev = dummyNode

        while True:

            kth = self.getkth(groupPrev, k)

            if not kth:
                break

            groupNext = kth.next

            # 0 -> 1 -> 2 (kth) | -> groupNext (3)
            #  2 -> 1 -> 3
            
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummyNode.next

    def getkth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr

            