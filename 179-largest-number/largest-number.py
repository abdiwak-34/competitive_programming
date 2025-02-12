class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        zero = nums.count(0)
        if zero == len(nums):
            return '0'
        def needswap(a,b):
            if b+a > a+b:
                return True
            return False
        nums2 = []
        for num in nums:
            nums2.append(str(num))
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if needswap(nums2[i],nums2[j]):
                    nums2[i], nums2[j] = nums2[j],nums2[i]
        return ''.join(nums2)