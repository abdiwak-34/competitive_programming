class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(a,b,sign):
            if sign == '+':
                return a + b
            elif sign == '-':
                return a - b
            elif sign == '*':
                return a * b
            else:
                return a / b
        stack = []
        for tok in tokens:
            if tok in '+-*/':
                b = stack.pop()
                a = stack.pop()
                stack.append(calculate(int(a),int(b),tok))
            else:
                stack.append(tok)
        return int(stack[0])