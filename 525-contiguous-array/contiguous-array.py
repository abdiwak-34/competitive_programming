class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {0:-1}
        presum = 0
        maximum = 0
        for i in range(len(nums)):
            presum += 1 if nums[i] == 1 else -1
            if presum in dic:
                maximum = max(maximum, i - dic[presum])
            else:
                dic[presum] = i
        return maximum