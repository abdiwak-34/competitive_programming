# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        def sumup(node1, node2, carry):
            nonlocal head
            if not node1 and not node2 and not carry:
                return
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            sums = val1 + val2 + carry
            node = ListNode(sums%10)
            head.next = node
            head = head.next

            sumup(node1.next if node1 else None, node2.next if node2 else None, sums//10)
        sumup(l1,l2,0)
        return dummy.next
