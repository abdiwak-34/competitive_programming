class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtrack(ind, subs):
            if ind == len(nums):
                answer.append(subs[:])
                return

            subs.append(nums[ind])
            backtrack(ind+1, subs)
            subs.pop()
            backtrack(ind+1, subs)
        backtrack(0,[])
            
        return answer