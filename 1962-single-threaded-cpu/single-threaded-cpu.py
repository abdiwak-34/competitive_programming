class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks2 = []
        heap = []
        ans = []
        for i, task in enumerate(tasks):
            tasks2.append((task[0], task[1], i))
        
        tasks2.sort(reverse= True)
        time = 0
        while tasks2 or heap:
            while tasks2 and tasks2[-1][0] <= time:
                a,b,c = tasks2.pop()
                heappush(heap, (b,c,a))

            if heap:
                a,b,c = heappop(heap)
                time += a
                ans.append(b)
            else:
                dif = tasks2[-1][0] - time
                time += dif
        
        return ans