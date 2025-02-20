# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge = ListNode()
        add =merge
        while list1 and list2:
            if list1.val <= list2.val:
                add.next = list1
                list1 = list1.next
            else:
                add.next = list2
                list2 = list2.next
            add = add.next
        if list1:
            add.next = list1
        if list2:
            add.next = list2
        return merge.next