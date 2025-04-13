class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited[city] = True
            for neighbour in range(len(isConnected)):
                if isConnected[city][neighbour] == 1 and not visited[neighbour]:
                    dfs(neighbour)

        province = 0
        visited = [False] * len(isConnected)

        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                province += 1
        return province
