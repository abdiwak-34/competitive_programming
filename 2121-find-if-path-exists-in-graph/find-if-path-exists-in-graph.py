class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for v, u in edges:
            graph[v].append(u)
            graph[u].append(v)
        
        def dfs(node, visted):
            visted.add(node)
            if node == destination:
                return True
            
            visted.add(node)

            for neighbour in graph[node]:
                if neighbour not in visted:
                    found = dfs(neighbour, visted)
                    if found:
                        return True
            return False
        
        return dfs(source, set())