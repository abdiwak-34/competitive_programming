class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        minH = []
        for i in range(len(grid)):
            row = grid[i]
            limit = limits[i]
            row.sort(reverse= True)

            for j in range(min(len(row), limit)):
                heappush(minH, row[j])

                if len(minH) > k:
                    heappop(minH)

        return sum(minH)