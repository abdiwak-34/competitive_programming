class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = defaultdict(int)
        for ind, num in enumerate(nums):
            hsh[target-num] = ind

        for ind, num in enumerate(nums):
            if num in hsh and hsh[num] != ind:
                return [hsh[num], ind]