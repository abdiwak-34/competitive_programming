class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] ==nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        zero = 0
        for i in range(len(nums)):
            if nums[zero] == 0 and nums[i] != 0:
                nums[zero],nums[i] = nums[i], nums[zero]
                zero += 1
            if nums[zero] != 0:
                zero += 1
        return nums
