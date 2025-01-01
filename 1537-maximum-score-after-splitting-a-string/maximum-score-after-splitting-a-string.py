class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0 
        sumation = 0
        for i in range(len(s)):
            sumation += int(s[i])
        for left in range(len(s) - 1):
            if s[left] == '0':
                sumation +=1
            else:
                sumation -= 1
            max_score = max(max_score, sumation)
        return max_score