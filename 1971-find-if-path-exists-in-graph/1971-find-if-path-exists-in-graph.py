class Solution(object):
    def validPath(self, n, edges, source, destination):
        adj =[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[False]*n

        def dfs(node):
            if node == destination:
                return True
            visited[node] = True
            for nei in adj[node]:
                if not visited[nei]:
                    if dfs(nei):
                        return True
            return False
        return dfs(source)
        