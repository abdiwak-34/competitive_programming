class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        
        for i in range(n):
            while stack and prices[i] <= prices[stack[-1]]:
                idx = stack.pop()
                prices[idx] -= prices[i]
            stack.append(i)
        
        return prices
