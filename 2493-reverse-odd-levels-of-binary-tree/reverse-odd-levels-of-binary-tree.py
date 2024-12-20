# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def depth(node1, node2, level):
            if not node1 or not node2:
                return
            
            if level % 2 == 1:
                node1.val, node2.val = node2.val, node1.val
            
            depth(node1.left, node2.right, level + 1)
            depth(node1.right, node2.left, level + 1)
    
        if not root:
            return root
        
        depth(root.left, root.right, 1)
        return root