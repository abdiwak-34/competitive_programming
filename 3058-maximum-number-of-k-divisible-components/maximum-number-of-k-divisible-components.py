class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        result = 0
        
        def dfs(node):
            nonlocal result
            visited.add(node)
            subtree_sum = values[node]
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    subtree_sum += dfs(neighbor)
            if subtree_sum % k == 0:
                result += 1
                return 0
            
            return subtree_sum
        
        dfs(0)
        return result