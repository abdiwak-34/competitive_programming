class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = (len(piles)//3) * 2
        sum_of = 0
        for i in range(1,n,2):
            sum_of += piles[i]
        return sum_of