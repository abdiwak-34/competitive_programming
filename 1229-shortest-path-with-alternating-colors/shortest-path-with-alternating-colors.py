class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for a, b in redEdges:
            red_graph[a].append(b)
        for a, b in blueEdges:
            blue_graph[a].append(b)

        ans = [-1] * n
        queue = deque([(0, 0), (0, 1)])
        visited = set(queue)
        dist = 0

        while queue:
            for _ in range(len(queue)):
                node, color = queue.popleft()

                if ans[node] == -1:
                    ans[node] = dist
                else:
                    ans[node] = min(ans[node], dist)

                if color == 0:
                    for child in blue_graph[node]:
                        if (child, 1) not in visited:
                            visited.add((child, 1))
                            queue.append((child, 1))
                else:
                    for child in red_graph[node]:
                        if (child, 0) not in visited:
                            visited.add((child, 0))
                            queue.append((child, 0))
            dist += 1

        return ans