# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right= dummy
        for i in range(n):
            right = right.next
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next