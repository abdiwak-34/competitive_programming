# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = first
            first = cur
            cur = next_node
        return first