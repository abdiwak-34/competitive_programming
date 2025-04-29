class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        n= len(matrix)
        for i in range(n):
            for j in range(n):
                heappush(arr, -matrix[i][j])
                if len(arr)>k:
                    heappop(arr)
        return -arr[0]