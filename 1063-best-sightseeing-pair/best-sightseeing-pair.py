class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        sightsee = float('-inf')
        max_so_far = values[0] - 1
        for i in range(1,len(values)):
            sightsee = max(sightsee, max_so_far + values[i])
            max_so_far = max(max_so_far, values[i]) - 1
        return sightsee