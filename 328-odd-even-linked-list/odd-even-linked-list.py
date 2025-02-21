# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        head_odd = odd
        head_even = even
        current = head
        count = 1
        while current:
            if count % 2 == 1:
                odd.next = current
                odd = odd.next
            else:
                even.next = current
                even = even.next
            current = current.next
            count += 1
        even.next = None
        odd.next = head_even.next
        return head_odd.next
