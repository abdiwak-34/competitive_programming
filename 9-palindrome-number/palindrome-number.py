class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if x<0 :
            return False
        for i in range(len(s)-1//2):
            if s[i]!= s[len(s)-1-i]:
             return False
        return True