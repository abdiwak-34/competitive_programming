class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] *= 2
                nums[i] = 0
        left = 0
        for right in range(len(nums)):
            while nums[left] != 0 and left < right:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]
        return nums