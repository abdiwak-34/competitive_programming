class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = max(citations)
        count = [0]* (n+1)
        for citation in citations:
            count[citation] += 1
        count = count[::-1]
        for i in range(1,len(count)):
            count[i] += count[i-1]
        print(count)
        for ind,val in enumerate(count):
            if val >= n-ind:
                return n-ind
