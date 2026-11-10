# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merged(list1, list2):
            dummyNode = ListNode()
            tail = dummyNode

            while list1 and list2:
                if list1.val > list2.val:
                    tail.next = list2
                    list2 = list2.next
                else:
                    tail.next = list1
                    list1 = list1.next
                tail = tail.next
            
            if list1:
                tail.next = list1
            if list2:
                tail.next = list2  
            return dummyNode.next

        while len(lists) > 1:
            merge_list = []
            for i in range(0, len(lists), 2):
                lst1 = lists[i] 
                lst2 = lists[i+1] if i+1 < len(lists) else None
                merge_list.append(merged(lst1,lst2))
            lists = merge_list
        return lists[0]