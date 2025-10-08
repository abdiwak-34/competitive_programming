class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hsh = defaultdict(int)
        hsh[0] = 1
        presum = 0
        count = 0
        for i in range(len(nums)):
            presum += nums[i]
            if (presum - k) in hsh:
                count += hsh[presum-k]
            hsh[presum] += 1
        
        return count