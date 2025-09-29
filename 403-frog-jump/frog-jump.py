class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        n = len(stones)
        memo = set()
        def dp(idx, prev):
            if idx == n - 1:
                return True
            if prev == 0:
                return False
            if (idx, prev) in memo:
                return False
            #prev - 1
            req =  stones[idx] + prev - 1
            left = bisect_left(stones,req)
            if left < n and stones[left] == req:
                if dp(left, prev - 1):
                    return True
            #prev
            req =  stones[idx] + prev
            left = bisect_left(stones,req)
            if left < n and stones[left] == req:
                if dp(left, prev):
                    return True
            #prev + 1
            req =  stones[idx] + prev + 1
            left = bisect_left(stones,req)
            if left < n and stones[left] == req:
                if dp(left, prev + 1):
                    return True
            memo.add((idx, prev))
            return False
        return dp(1, 1)