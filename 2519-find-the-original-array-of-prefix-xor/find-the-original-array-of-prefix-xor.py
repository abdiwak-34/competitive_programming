class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        pre = 0
        ans = []
        for num in pref:
            ans.append(pre ^ num)
            pre = num
        return ans