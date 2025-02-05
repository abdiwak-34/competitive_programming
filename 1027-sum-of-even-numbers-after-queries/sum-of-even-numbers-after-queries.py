class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sumof = 0
        for x in nums:
            if x%2 == 0:
                sumof += x
    
        for query in queries:
            v, i = query
            k = nums[i] + v
            if k %2 == 0 and v %2 == 0:
                sumof += v
            elif k %2 == 0 and v %2 != 0:
                sumof += (nums[i] + v)
            elif k %2 != 0 and v %2 != 0:
                sumof -= nums[i]
            nums[i] += v
            ans.append(sumof)
        return ans