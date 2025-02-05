class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for key in count:
            if count[key] == 2:
                ans.append(key)
        return ans