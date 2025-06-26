class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            queue = deque([(start, 1.0)])
            visited = set()
            visited.add(start)
            while queue:
                node, current_product = queue.popleft()
                if node == end:
                    return current_product
                for neighbor, weight in graph[node].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_product * weight))
            return -1.0
        
        results = []
        for query in queries:
            start, end = query
            results.append(bfs(start, end))
        return results