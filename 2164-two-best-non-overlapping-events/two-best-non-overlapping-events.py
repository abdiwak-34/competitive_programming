class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)
        ends = [event[1] for event in events]
        max_so_far = [0] * n
        max_value = 0
        
        for i in range(n):
            start, end, value = events[i]
            idx = bisect.bisect_right(ends, start - 1) - 1
            combined_value = value + (max_so_far[idx] if idx >= 0 else 0)
            max_value = max(max_value, combined_value)
            max_so_far[i] = max(max_so_far[i - 1], value) if i > 0 else value
        
        return max_value