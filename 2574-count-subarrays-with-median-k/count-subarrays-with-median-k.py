class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        pos = nums.index(k)
        bal = 0
        for i in range(pos+1, len(nums)):
            bal += 1 if nums[i] > k else -1
            count[bal] += 1

        ans = 0
        bal = 0
        for i in range(pos,-1,-1):
            bal += 1 if nums[i] > k else (-1 if nums[i] < k else 0)
            ans += count[-bal]
            ans += count[-bal+1]
        return ans