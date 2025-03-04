class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = l = count = 0
        for i in range(len(s)):
            r += int(s[i] == 'R')
            l += int(s[i] == 'L')
            if l == r:
                count += 1
                l = r = 0
        return count