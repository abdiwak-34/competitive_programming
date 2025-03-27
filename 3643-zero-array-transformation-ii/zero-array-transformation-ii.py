class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def possible(num):
            n = len(nums)
            diff = [0] * n
            for i in range(num):
                s,e,v = queries[i]
                diff[s] -= v
                if e + 1 < n:
                    diff[e+1] += v
            for j in range(1,n):
                diff[j] += diff[j-1]
            for k in range(n):
                diff[k] += nums[k]
                if diff[k] > 0:
                    return False
            return True
        if nums.count(0) == len(nums):
            return 0
        left, right = 0, len(queries)-1
        best = -1
        while left <= right:

            mid = (left+right)//2
            if possible(mid+1):
                best = mid+1
                right = mid - 1
            else:
                left = mid + 1
        return best