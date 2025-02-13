class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)
        
        for i in range(n,0,-1):
            left = 0
            while left < i and arr[left] != i:
                left +=1
            arr[:left+1] = arr[:left+1][::-1]
            arr[:i] = arr[:i][::-1]
            ans.append(left+1)
            ans.append(i)
        return ans