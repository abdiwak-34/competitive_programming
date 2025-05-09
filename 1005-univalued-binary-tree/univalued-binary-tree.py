# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, node: Optional[TreeNode]) -> bool:
        uni = node.val
        queue = deque([node])
        while queue:
            for nodes in range(len(queue)):
                current = queue.popleft()
                if current.val != uni:
                    return False
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return True
