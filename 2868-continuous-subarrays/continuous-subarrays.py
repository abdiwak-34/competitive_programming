class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        max_que = deque()
        min_que = deque()
        count = left = 0
        for right in range(len(nums)):
            while max_que and nums[max_que[-1]] <= nums[right]:
                max_que.pop()
            max_que.append(right)
            while min_que and nums[min_que[-1]] >= nums[right]:
                min_que.pop()
            min_que.append(right)
            while abs(nums[max_que[0]] - nums[min_que[0]]) > 2:
                left += 1
                if max_que[0] < left:
                    max_que.popleft()
                if min_que[0] < left:
                    min_que.popleft()
            count += (right - left + 1)
        return count