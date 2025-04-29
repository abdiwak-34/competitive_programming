from heapq import heappush, heappop
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i,head in enumerate(lists):
            if head:
                heappush(arr, (head.val,i, head))
        dummy = ListNode()
        cur = dummy
        while arr:
            val,ind, node = heappop(arr)
            cur.next = node
            cur = cur.next
            if node.next:
                heappush(arr, (node.next.val, ind, node.next))
            
        return dummy.next


        