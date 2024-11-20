class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ('a','e','i','o','u')
        maximum = j = count = 0
        while j < k-1:
            if s[j] in vowel:
                count += 1
            j += 1
        for i in range(len(s)):
            if j < len(s) and s[j] in vowel:
                count += 1
            maximum = max(maximum,count)
            if s[i] in vowel:
                count -= 1
            j += 1
        return maximum             
