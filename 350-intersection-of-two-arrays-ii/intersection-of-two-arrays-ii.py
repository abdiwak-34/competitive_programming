class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = []
        left = right = 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                intersection.append(nums1[left])
                left += 1
                right +=1 
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        return intersection