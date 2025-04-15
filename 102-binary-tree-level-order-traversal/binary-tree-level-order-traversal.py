# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        ans = []
        while queue:
            level = []
            for i in range(len(queue)):

                current = queue.popleft()
                if current:
                    level.append(current.val)
                if current and current.left:
                    queue.append(current.left)
                if current and current.right:
                    queue.append(current.right)
            if level:
                ans.append(level)
        return ans