class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ptr = 0
        while ptr < len(costs):
            if coins >= costs[ptr]:
                coins -= costs[ptr]
                ptr += 1
            else:
                return ptr
        return ptr