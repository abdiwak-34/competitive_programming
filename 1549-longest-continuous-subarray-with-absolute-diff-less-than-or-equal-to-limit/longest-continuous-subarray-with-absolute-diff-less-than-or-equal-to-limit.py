class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increase = deque()
        decrease = deque()
        left = maximum = 0
        for right in range(len(nums)):
            while increase and increase[-1] > nums[right]:
                increase.pop()
            
            while decrease and decrease[-1] < nums[right]:
                decrease.pop()
            increase.append(nums[right])
            decrease.append(nums[right])
            while decrease[0] - increase[0] > limit:
                if nums[left] == increase[0]:
                    increase.popleft()
                if nums[left] == decrease[0]:
                    decrease.popleft()
                left += 1
            maximum = max(maximum, right-left +1)

        return maximum