class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        My_coin = 0
        for i in range(1,2*(len(piles)//3), 2):
            My_coin += piles[i]
        return My_coin