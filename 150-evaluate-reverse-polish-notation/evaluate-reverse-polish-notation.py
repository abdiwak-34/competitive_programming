class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                A = stack.pop()
                B = stack.pop()

                if i == '+':
                    stack.append(A+B)
                elif i == '-':
                    stack.append(B-A)
                elif i == '*':
                    stack.append(A*B)
                elif i == '/':
                    stack.append(int(B/A))
        return stack.pop()