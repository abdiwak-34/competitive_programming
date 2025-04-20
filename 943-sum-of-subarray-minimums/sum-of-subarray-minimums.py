class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack, result = [], 0
        arr = [0] + arr + [0]

        for i, v in enumerate(arr):
            while stack and arr[stack[-1]] > v:
                mid = stack.pop()
                left = mid - stack[-1]
                right = i - mid
                result += arr[mid] * left * right
            stack.append(i)

        return result % MOD
