import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hsh = Counter(answers)
        ans = 0
        nums = set(answers)
        for num in nums:
            ans += (num + 1) * math.ceil(hsh[num] / (num + 1))
        return ans