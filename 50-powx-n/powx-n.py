class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(n):
            if n == 0:
                return 1
            if n %2 == 0:
                res = power(n//2)
                return res * res
            return x * power(n-1)
        if n < 0:
            n = abs(n)
            return 1/power(n)
        return power(n)
