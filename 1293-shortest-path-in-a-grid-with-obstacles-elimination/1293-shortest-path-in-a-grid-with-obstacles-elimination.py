class Solution(object):
    def shortestPath(self, grid, k):
        m=len(grid)
        n=len(grid[0])
        queue=[]
        queue.append([0,0,0,k])

        visited = set()
        visited.add((0,0,k))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            row,col,steps,state=queue.pop(0)

            if row == m-1 and col == n-1:
                return steps
            
            for dir in directions:
                nr = row+dir[0]
                nc = col+dir[1]

                if nr<0 or nr>=m or nc<0 or nc>=n:
                    continue
                
                newState = state

                if grid[nr][nc] == 1:
                    newState -=1

                if newState < 0:
                    continue

                if (nr,nc,newState) in visited:
                    continue

                visited.add((nr,nc,newState))
                queue.append([nr,nc,steps+1,newState])
        return -1



        