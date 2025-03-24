class Solution:
    def findleft(self, nums, target):
        ans = -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                ans = mid
            if nums[mid] < target:
                left = mid +1
            else:
                right = mid -1
        return ans 

    def findright(self, nums, target):
        ans = -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                ans = mid
            if nums[mid] > target:
                right = mid -1
            else:
                left = mid +1
        return ans 
    def searchRange(self, nums: List[int], target: int) -> List[int]:
         return [self.findleft(nums, target),self.findright(nums,target)]