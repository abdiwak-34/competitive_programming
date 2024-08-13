class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        coverage = [0] * 51
        for start, end in ranges:
            for i in range(start, end + 1):
                coverage[i] = 1
        for i in range(left, right + 1):
            if coverage[i] == 0:
                return False
        
        return True
