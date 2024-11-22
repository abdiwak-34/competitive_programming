class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            new = int(i)
            while k > 0 and stack and stack[-1] > new:
                stack.pop()
                k-= 1
            stack.append(new)
        stack = stack[:-k] if k > 0 else stack
        result = ''.join(map(str, stack)).lstrip('0')
        
        return result if result else "0"