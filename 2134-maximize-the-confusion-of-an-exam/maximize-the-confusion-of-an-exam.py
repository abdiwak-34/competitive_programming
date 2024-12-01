class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        no_true = left = no_false = ans = 0
        for i in range(len(answerKey)):
            if answerKey[i] == 'T':
                no_true += 1
            no_false = (i-left+1) - no_true
            if (no_true >= no_false and no_false <= k) or (no_false > no_true and no_true <= k):               ans = max(ans, no_true + no_false)
            else:
                if answerKey[left] == "T":
                    no_true -= 1
                left += 1
        return ans