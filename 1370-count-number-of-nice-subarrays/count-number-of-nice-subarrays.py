class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        presum = ans = 0
        count[0] = 1
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                presum += 1
            if (presum - k) in count:
                ans += count[presum-k]
            count[presum] +=1
        return ans