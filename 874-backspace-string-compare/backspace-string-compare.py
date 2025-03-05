class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        for i in s:
            if stack1 and i == '#':
                stack1.pop()
            elif i != '#':
                stack1.append(i)
        stack2 = []
        for j in t:
            if stack2 and j == '#':
                stack2.pop()
            elif j != '#':
                stack2.append(j)
        return stack1 == stack2