class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         nums1 += nums2
         nums1.sort()
         med = 0
         if len(nums1) % 2 == 0:
            med = (nums1[(len(nums1) - 1) // 2] + nums1[len(nums1) // 2]) / 2
         else :
            med = nums1[(len(nums1) - 1) // 2]
         return med