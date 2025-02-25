class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n= len(arr)
        def find(arr):
            inter = [0] * n
            count = defaultdict(int)
            prev = defaultdict(int)
            for i in range(n):
                if arr[i] in prev:
                    no = count[arr[i]] -1
                    dist = i - prev[arr[i]]
                    inter[i] += (inter[prev[arr[i]]] + (no * dist) + dist)
                prev[arr[i]] = i
                count[arr[i]] += 1
            return inter
        forward = find(arr)
        rev = arr.reverse()
        backward = find(arr)
        backward.reverse()
        for i in range(n):
            forward[i] += backward[i]

        return forward