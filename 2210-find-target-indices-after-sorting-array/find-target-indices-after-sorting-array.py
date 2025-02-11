class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count_targ = 0
        count_no = 0
        ans = []
        for num in nums:
            if num < target:
                count_no += 1
            elif num == target:
                count_targ += 1
        for j in range(count_no, count_no + count_targ):
            ans.append(j)
        return ans