class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def max_cons(chr):
            flip = 0
            max_conf = 0
            left = 0
            for i in range(len(answerKey)):
                if answerKey[i] != chr:
                    flip += 1
                while flip > k:
                    if answerKey[left] != chr:
                        flip -= 1
                    left += 1
                max_conf = max(max_conf, i-left+1)
            return max_conf
        return max(max_cons('T'), max_cons('F'))