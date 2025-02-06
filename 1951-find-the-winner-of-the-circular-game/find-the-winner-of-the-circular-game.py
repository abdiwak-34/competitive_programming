class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [x for x in range(1, n+1)]
        left = 0
        while len(arr) >1:
            left = (left + k-1)%len(arr)
            arr.remove(arr[left])
        return arr[0]