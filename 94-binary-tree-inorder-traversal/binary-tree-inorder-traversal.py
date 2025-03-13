# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,node, res):
            if not node:
                return res
            self.inorder(node.left,res)
            res.append(node.val)
            self.inorder(node.right,res)
            return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root,[])