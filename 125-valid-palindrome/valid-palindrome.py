class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        for i in s:
            if i in "abdcdefghijklmnopqrstuvwxyz0123456789":
                new_s += i
        return True if new_s == new_s[::-1] else False