class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def possible(subsum):
            count= 1
            sub = 0
            for i in range(len(nums)):
                if nums[i] > subsum:
                    return False
                if sub + nums[i] > subsum:
                    count += 1
                    sub = nums[i]
                else:
                    sub += nums[i]
            return count <= k
        
        left, right = 0,sum(nums)
        best = right
        while left <= right:
            mid = (left+right)//2
            if possible(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best