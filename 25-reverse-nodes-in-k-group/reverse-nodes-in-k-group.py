# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = head
        size = 0
        while current:
            size +=1 
            current = current.next
        
        def reverse(head1):
            end = head1.next
            current = head1.next
            for i in range(k):
                nextNode = current.next
                current.next = head1.next
                head1.next = current
                current = nextNode
            end.next = current
            return end
        heads = dummy
        for i in range(size // k):
            heads = reverse(heads)
        return dummy.next