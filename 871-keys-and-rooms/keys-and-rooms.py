class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visit = [False] * n

        queue = deque([0])
        while queue:
            room = queue.popleft()
            visit[room] = True
            for r in rooms[room]:
                if not visit[r]:
                    queue.append(r)
        
        return all(visit)