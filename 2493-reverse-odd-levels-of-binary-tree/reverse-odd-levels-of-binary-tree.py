# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level = 1
        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            if level %2:
                left, right = 0, len(queue)-1
                while left < right:
                    queue[left].val, queue[right].val = queue[right].val, queue[left].val
                    left +=1
                    right -= 1
            level += 1
        return root