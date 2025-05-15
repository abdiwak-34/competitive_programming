class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pre = 0
        for num in nums:
            pre = pre ^ num
        return pre