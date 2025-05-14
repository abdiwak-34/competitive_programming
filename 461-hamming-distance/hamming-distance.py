class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x^y
        return z.bit_count()