# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        array = []
        def find(node, depth):
            if not node:
                return
            if depth < len(array):
                array[depth] = max(array[depth], node.val)
            else:
                array.append(node.val)
            find(node.left, depth+1)
            find(node.right, depth+1)
        
        find(root, 0)
        return array