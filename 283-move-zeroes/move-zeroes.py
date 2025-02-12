class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(1,len(nums)):
            while left < right and nums[left] != 0:
                left += 1
            if nums[left] == 0:
                nums[right], nums[left] = nums[left], nums[right]