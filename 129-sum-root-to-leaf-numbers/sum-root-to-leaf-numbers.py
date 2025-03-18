# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = []
        def find(node, nums):
            if node and not node.left and not node.right:
                ans.append(nums+str(node.val))
                return
            if not node:
                return
            nums += str(node.val)
            find(node.right, nums)
            find(node.left, nums)
        find(root, '')

        return sum(int(x) for x in ans)