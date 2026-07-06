class Solution(object):
    def maxAreaOfIsland(self, grid):
        rows=len(grid)
        cols=len(grid[0])
        self.count=0

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return
            if grid[r][c]==0:
                return
            
            grid[r][c]=0
            self.count+=1

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        ans=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    self.count=0
                    dfs(i,j)
                    ans=max(ans,self.count)
        return ans
        