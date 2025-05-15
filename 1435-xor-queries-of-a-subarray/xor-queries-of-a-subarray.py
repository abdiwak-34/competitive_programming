class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prexor = [arr[0]]
        ans = []
        for i in range(1, len(arr)):
            prexor.append(arr[i] ^ prexor[-1])
        for left, right in queries:
            if left-1 >= 0:
                ans.append(prexor[right] ^ prexor[left-1])
            else:
                ans.append(prexor[right])
        return ans