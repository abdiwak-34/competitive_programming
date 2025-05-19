class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = reduce(xor, nums1) if len(nums2) % 2 == 1 else 0
        xor2 = reduce(xor, nums2) if len(nums1) % 2 == 1 else 0
        return xor1 ^ xor2