class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = left = 0
        subst = set()
        for right in range(len(s)):
            while s[right] in subst:
                subst.remove(s[left])
                left += 1
            subst.add(s[right])
            longest = max(longest, right-left + 1)
        return longest