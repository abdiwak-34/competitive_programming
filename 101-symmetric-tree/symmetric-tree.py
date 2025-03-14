# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mirror(self,nleft, nright):
        if not nleft and not nright:
            return True
        if not nleft or not nright:
            return False
        return nleft.val == nright.val and self.mirror(nleft.left, nright.right) and self.mirror(nleft.right, nright.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirror(root,root)