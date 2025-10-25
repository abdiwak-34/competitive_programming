class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def inbound(inde):
            return 0 <= inde < len(arr)
        visted = [False] * len(arr)
        queue = deque([start])
        visted[start] = True

        while queue:
            ind = queue.popleft()
            if arr[ind] == 0:
                return True
            
            if inbound(ind+arr[ind]) and not visted[ind+arr[ind]]:
                queue.append(ind+arr[ind])
                visted[ind+arr[ind]] = True
            if inbound(ind-arr[ind]) and not visted[ind-arr[ind]]:
                queue.append(ind-arr[ind])
                visted[ind-arr[ind]] = False
        return False
