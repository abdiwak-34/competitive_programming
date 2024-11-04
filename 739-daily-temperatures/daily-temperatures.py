class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            # warm = i
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre = stack.pop()
                ans[pre] = i - pre
            stack.append(i)    
        return ans