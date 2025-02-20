# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tor = head
        rabbit = head
        while rabbit and tor and rabbit.next:
            rabbit = rabbit.next.next
            tor = tor.next

            if rabbit == tor:
                return True
        return False