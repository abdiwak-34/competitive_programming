class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for num in range(2**len(nums)):
            temp = []
            for i in range(len(nums)):
                if num & (1 << i) != 0:
                    temp.append(nums[i])
            ans.append(temp)
        return ans