# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        left = right = head
        while right and right.next:
            right = right.next.next
            left = left.next
            if right == left:
                return True
        return False