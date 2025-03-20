# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find(node, sums):
            if not node:
                return 0 + sums
            right = find(node.right, sums)
            node.val += right
            left = find(node.left,node.val)
            return left
        find(root,0)
        return root