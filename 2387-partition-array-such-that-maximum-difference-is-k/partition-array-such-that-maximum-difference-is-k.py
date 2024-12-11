class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        count = 1
        for right in range(len(nums)):
            if nums[right] - nums[left] > k:
                left = right
                count += 1
        return count