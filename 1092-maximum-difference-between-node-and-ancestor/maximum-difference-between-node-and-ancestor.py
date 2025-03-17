# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def finder(node, minimum, maximum):
            if not node:
                return maximum - minimum
            
            minimum = min(minimum, node.val)
            maximum = max(maximum, node.val)

            return max(finder(node.left, minimum, maximum), finder(node.right, minimum, maximum))
            
        return finder(root,root.val, root.val)