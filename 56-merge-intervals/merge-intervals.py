class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for i in range(len(intervals)):
            if ans and ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = intervals[i][1] if intervals[i][1] > ans[-1][1] else ans[-1][1]
            else:
                ans.append(intervals[i])

        return ans