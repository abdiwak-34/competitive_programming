class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        def delta(p,t):
            return (p+1)/(t+1) - p/t
        for clas in classes:
            p, t = clas
            delta1 = delta(p, t)
            heapq.heappush(heap, (-delta1,p,t))
        for i in range(extraStudents):
            delta2, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            new_del = delta(p, t)
            heapq.heappush(heap, (-new_del, p, t))
        total = 0
        while heap:
            delta3, p, t = heapq.heappop(heap)
            total += p/t
        return total/len(classes)