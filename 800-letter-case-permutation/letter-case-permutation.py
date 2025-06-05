class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = ['']
        for char in s:
            if char.isalpha():
                ans = [pref + c for pref in ans for c in [char.lower(), char.upper()]]
            else:
                ans = [pref + char for pref in ans]
        return ans