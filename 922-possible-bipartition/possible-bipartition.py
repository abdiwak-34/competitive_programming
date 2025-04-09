class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1] * (n+1)
        graph = defaultdict(list)
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node,c):
            color[node] = c

            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    if not dfs(neighbour,1-c):
                        return False
                elif color[neighbour] == color[node]:
                    return False
            return True
        
        for i in range(1,n+1):
            if color[i] == -1:
                if not dfs(i,0):
                    return False
        return True