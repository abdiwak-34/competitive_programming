# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def find(node,sums):
            if not node:
                return False
            
            sums += node.val
            if not node.left and not node.right:
                return sums == targetSum
            return find(node.left,sums) or find(node.right,sums)
        return find(root,0)