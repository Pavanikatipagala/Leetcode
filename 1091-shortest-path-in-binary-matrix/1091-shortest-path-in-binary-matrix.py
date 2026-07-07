class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0]==1 or grid[n-1][n-1] ==1:
            return -1

        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        q= deque()
        q.append((0,0,1))
        grid[0][0]=1

        while q :
            r,c,d = q.popleft()

            if r == n-1 and c == n-1 :
                return d

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc

                if (0 <= nr < n and  0<= nc <n and grid[nr][nc]==0):
                    grid[nr][nc] = 1

                    q.append((nr,nc,d+1))
        return -1
