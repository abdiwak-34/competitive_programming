class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ubits = 0
        left = 0
        maxlen = 0

        for right in range(len(nums)):
            while ubits & nums[right]:
                ubits ^= nums[left]
                left += 1
            ubits |= nums[right]
            maxlen = max(maxlen, right - left + 1)

        return maxlen