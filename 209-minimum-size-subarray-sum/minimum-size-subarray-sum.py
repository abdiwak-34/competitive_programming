class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        ans = len(nums)
        left = summa = 0
        for i in range(len(nums)):
            summa += nums[i]
            while left <= i and summa >= target:
                ans = min(ans, i - left + 1)
                summa -= nums[left]
                left += 1
        return ans