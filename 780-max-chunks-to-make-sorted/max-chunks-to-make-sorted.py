class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_chunk = count = 0
        for i in range(len(arr)):
            max_chunk = max(max_chunk, arr[i])
            if max_chunk == i:
                count += 1
        return count