class Solution:
    def isValid(self, s: str) -> bool:
        diction = {'}':'{',')':'(',']':'['}
        stack = []
        for i in s:
            if stack and i in diction and stack[-1] == diction[i]:
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0