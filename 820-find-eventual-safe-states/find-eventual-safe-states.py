class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph2 = defaultdict(list)
        outdegree = []
        for node, neighbor in enumerate(graph):
            outdegree.append(len(neighbor))
            for n in neighbor:
                graph2[n].append(node)
        
        queue = deque()
        for i, de in enumerate(outdegree):
            if de == 0:
                queue.append(i)
        
        answer = []
        while queue:
            for _ in range(len(queue)):
                nod = queue.popleft()
                answer.append(nod)
                for neigh in graph2[nod]:
                    outdegree[neigh] -= 1
                    if outdegree[neigh] == 0:
                        queue.append(neigh)
        return sorted(answer)