class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = {'a','e','i','o','u'}
        maximum = j = count = 0
        while j < k:
            if s[j] in vowel:
                count += 1
            j += 1
        maximum = count
        for i in range(k , len(s)):
            if s[i] in vowel:
                count += 1
            if s[i-k] in vowel:
                count -= 1
            maximum = max(maximum,count)
      
        return maximum             
