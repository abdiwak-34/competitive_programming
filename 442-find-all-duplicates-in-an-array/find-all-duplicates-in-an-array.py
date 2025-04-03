class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        left = 0
        while left < len(nums):
            pos = nums[left]-1
            if left != pos:
                if nums[left] == nums[pos]:
                    ans.add(nums[left])
                    left += 1
                else:
                    nums[left],nums[pos] = nums[pos],nums[left]
            else:
                left += 1
        return list(ans)