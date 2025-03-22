class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def find(perm):
            if len(perm) == len(nums):
                ans.append(perm[:])
                return
            for i in range(len(nums)):
                if nums[i] not in perm:
                    perm.append(nums[i])
                    find(perm)
                    perm.pop()
        find([])
        return ans