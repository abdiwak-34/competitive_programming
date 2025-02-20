# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        greater = ListNode()
        temp = less
        temp2 = greater
        while head:
            if head.val >= x:
                greater.next = ListNode(head.val)
                greater = greater.next
            else:
                less.next = ListNode(head.val)
                less = less.next
            head = head.next
        less.next = temp2.next
        return temp.next


