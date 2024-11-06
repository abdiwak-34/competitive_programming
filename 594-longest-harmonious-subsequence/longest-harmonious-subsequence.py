class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_length = 0
        for i in count:
            if i + 1 in count:
                max_length = max(max_length, count[i]+count[i+1])
        return max_length
