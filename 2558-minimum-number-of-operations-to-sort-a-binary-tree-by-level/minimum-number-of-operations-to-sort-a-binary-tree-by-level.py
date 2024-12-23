# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def minSwapsToSort(arr):
            indexed_arr = sorted((value, index) for index, value in enumerate(arr))
            visited = [False] * len(arr)
            swaps = 0

            for i in range(len(arr)):
                if visited[i] or indexed_arr[i][1] == i:
                    continue
                cycle_size = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = indexed_arr[j][1]
                    cycle_size += 1
                if cycle_size > 1:
                    swaps += cycle_size - 1

            return swaps
        if not root:
            return 0
        queue = deque([root])
        levels = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        operations = 0
        for level in levels:
            operations += minSwapsToSort(level)

        return operations