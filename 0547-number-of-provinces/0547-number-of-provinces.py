class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i]:
                self.dfs(i,visited,isConnected)
                count +=1
        return count
    
    def dfs(self,node,visited,isConnected):
        n = len(isConnected)
        visited[node]=True
        for neighbor in range(n):
            if not visited[neighbor] and isConnected[node][neighbor]==1:
                self.dfs(neighbor,visited,isConnected)