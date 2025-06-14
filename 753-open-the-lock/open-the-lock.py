class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1

        visited = set("0000")
        queue = deque([("0000", 0)])

        while queue:
            cur, turns = queue.popleft()

            if cur == target:
                return turns

            for i in range(4):
                for d in (-1,1):
                    next_lis = list(cur)
                    next_lis[i] = str((int(next_lis[i]) + d) % 10)
                    next_str = ''.join(next_lis)
                    if next_str not in dead and next_str not in visited:
                        visited.add(next_str)
                        queue.append((next_str, turns + 1))
                    
        return -1