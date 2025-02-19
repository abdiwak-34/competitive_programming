class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        presum = 0
        result = 0
        for i in range(len(nums)):
            presum += nums[i]
            if presum - goal in count:
                result += count[presum-goal]
            count[presum] += 1
        return result