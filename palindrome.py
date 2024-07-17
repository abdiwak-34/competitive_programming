class Solution:
    def isPalindrome(self, x: int) -> bool:
         original_number = x
         reversed_number = 0

         while x > 0:
             digit = x % 10
             reversed_number = reversed_number * 10 + digit
             x = x // 10

         return original_number == reversed_number
        