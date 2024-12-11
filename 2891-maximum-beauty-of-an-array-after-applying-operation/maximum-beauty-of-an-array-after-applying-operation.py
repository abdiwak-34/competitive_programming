class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        maxim = 1
        left = 0
        nums.sort()
        for right in range(1,len(nums)):
            while nums[right] - nums[left] > 2*k:
                left += 1
            maxim = max(maxim, right - left + 1)
        return maxim