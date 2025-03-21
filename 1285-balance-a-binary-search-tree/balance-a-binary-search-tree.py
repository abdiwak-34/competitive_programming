# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sorted_arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            sorted_arr.append(node.val)
            inorder(node.right)
        inorder(root)
        print(sorted_arr)

        def construct(left, right):
            if left > right:
                return

            mid = (left+right)//2
            node = TreeNode(sorted_arr[mid])
            node.left = construct(left, mid-1)
            node.right = construct(mid+1, right)
            return node
        return construct(0, len(sorted_arr)-1)