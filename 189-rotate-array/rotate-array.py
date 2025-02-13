class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift = []
        k %= len(nums)
        for i in range(-k,0):
            shift.append(nums[i])
        for j in range(len(nums)-k-1,-1,-1):
            nums[j+k] = nums[j]
        for l in range(k):
            nums[l] = shift[l]