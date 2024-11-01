class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li = set()
        nums2_set = set(nums2)
        for i in nums1:
            if i in nums2_set:
                li.add(i)
        return list(li)