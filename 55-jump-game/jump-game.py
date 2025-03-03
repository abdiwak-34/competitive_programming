class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum = 0
        end = len(nums)-1
        for i in range(end+1):
            maximum = max(maximum, i + nums[i])
            if maximum == i and nums[i] == 0 and i != end:
                return False
            elif maximum >= end:
                return True
        return False