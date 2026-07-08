class Solution(object):
    def minCost(self, grid):
        m = len(grid)
        n = len(grid[0])

        queue=deque()
        queue.append([0, 0])

        directions = [[0,1,1],[0,-1,2],[1,0,3],[-1,0,4]]

        dist = [[float('inf')]* n for i in range(m)]
        dist[0][0] = 0

        while queue:
            curr = queue.popleft()

            row = curr[0]
            col = curr[1]

            for dir in directions:
                nr = row + dir[0]
                nc = col + dir[1]
                direction = dir[2]

                if nr< 0 or nr>=m or nc<0 or nc>=n:
                        continue
                
                cost =0

                if direction != grid[row][col]:
                    cost = 1

                if dist[nr][nc] > dist[row][col] + cost:
                    dist[nr][nc] = dist[row][col] + cost

                    if cost == 0:
                        queue.appendleft([nr, nc])
                    else:
                        queue.append([nr, nc])
  
        return dist[m-1][n-1]
                


                
        