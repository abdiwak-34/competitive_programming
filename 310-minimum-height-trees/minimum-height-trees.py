class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leav = [i for i in range(n) if len(graph[i]) == 1]

        rem_node = n
        while rem_node > 2:
            rem_node -= len(leav)
            new_leav = []
            for leaf in leav:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leav.append(neighbor)
            leav = new_leav

        return leav