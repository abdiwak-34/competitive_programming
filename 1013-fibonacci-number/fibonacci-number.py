class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict(int)
        def find(i):
            if i == 1 or i == 0:
                return i
            if i not in memo:
                memo[i] = find(i-1) + find(i-2)

            return memo[i]

        return find(n)