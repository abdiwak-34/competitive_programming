class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        answer = [x for x in range(len(quiet))]
        visited = [False] * len(quiet)
        for a,b in richer:
            graph[b].append(a)
        
        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for neighbor in graph[node]:

                dfs(neighbor)
                if quiet[answer[neighbor]] < quiet[answer[node]]:
                    answer[node] = answer[neighbor]

        for i in range(len(quiet)):
            dfs(i)
        return answer
        