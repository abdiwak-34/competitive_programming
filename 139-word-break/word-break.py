class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        set_words = set(wordDict)
        n = len(s)
        memo = {}
        def dp(left):
            if left >= n:
                return True
            if left in memo:
                return memo[left]
            for right in range(left + 1, n + 1):
                if s[left: right] in set_words:
                    if dp(right):
                        return True
            memo[left] = False
            return False
        return dp(0)