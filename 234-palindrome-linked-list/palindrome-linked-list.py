# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_rev = ListNode()
        current = head
        
        #reversing the list
        while current:
            newNode = ListNode(current.val)
            newNode.next = head_rev.next
            head_rev.next = newNode
            current = current.next
        head_rev = head_rev.next

        #checking if it is equal abdi
        while head_rev and head:
            if head_rev.val != head.val:
                return False
            head_rev = head_rev.next
            head = head.next
        return True