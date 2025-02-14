class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(t):
            left, right = 0, len(t)-1
            while left < right:
                if t[left] != t[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0,len(s)-1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome(s[left:right]) or is_palindrome(s[left+1:right+1])
            left += 1
            right -= 1
        return True