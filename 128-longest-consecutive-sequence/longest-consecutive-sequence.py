class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = 0
        for i in nums:
            j = 0
            if i - 1 not in nums_set:
                while i + j in nums_set:
                    j += 1 
            ans = max(ans, j)
        return ans