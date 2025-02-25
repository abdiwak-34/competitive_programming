# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur  = head
        trans = 0
        while l1 or l2:
            sums = 0
            if l1:
                sums += l1.val
                l1 = l1.next
            if l2:
                sums += l2.val
                l2 = l2.next
            sums += trans
            cur.next = ListNode(sums % 10)
            cur = cur.next
            trans = sums // 10
        if trans != 0:
            cur.next = ListNode(trans)
        return head.next
        

        return ans