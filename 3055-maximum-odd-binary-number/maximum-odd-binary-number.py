class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = s.count('1')
        m = len(s) - n
        return ('1' * (n-1)) + ('0' * m) + '1'