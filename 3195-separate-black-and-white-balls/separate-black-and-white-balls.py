class Solution:
    def minimumSteps(self, s: str) -> int:
        swap_black = operations = 0
        for i in range(len(s)):
            if s[i] == '0':
                operations += swap_black
            else:
                swap_black += 1
        return operations