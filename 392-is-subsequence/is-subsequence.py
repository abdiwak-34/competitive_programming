class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = count = 0
        for i in range(len(s)):
            while left < len(t) and s[i] != t[left]:
                left += 1
            if left< len(t) and s[i] == t[left]:
                left += 1
                count += 1
        return count == len(s)