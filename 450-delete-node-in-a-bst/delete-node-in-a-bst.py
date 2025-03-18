# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findminimum(node):
            while node.left:
                node = node.left
            return node

        
        def find(node,key):
            if not node:
                return node
            if node.val > key:
                node.left = find(node.left, key)
            elif node.val < key:
                node.right = find(node.right, key)

            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                temp = findminimum(node.right)

                node.val = temp.val
                node.right = find(node.right, temp.val)
            return node
        return find(root,key)
