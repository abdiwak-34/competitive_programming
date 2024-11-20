class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        left = maximum = right = 0
        while right < len(s):
            if ord(s[right]) - ord(s[right-1]) != 1:
                left = right
            maximum = max(maximum, right-left + 1)
            right += 1
        return maximum
            
            