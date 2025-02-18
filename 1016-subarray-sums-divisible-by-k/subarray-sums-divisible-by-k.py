class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder = defaultdict(int)
        remainder[0] = 1
        sums = count = 0
        remain = 0
        for i in range(len(nums)):
            sums += nums[i]
            remain = sums % k
            if remain < 0:
                remain += k
            if remain in remainder:
                count += remainder[remain]
            remainder[remain] += 1
        return count