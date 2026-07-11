class Solution(object):
    def shortestPathAllKeys(self, grid):
        m = len(grid)
        n = len(grid[0])

        startRow = 0
        startCol = 0
        k=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@':
                    startRow = i
                    startCol =j
                elif grid[i][j] >= 'a' and grid[i][j] <='f':
                    k +=1
        visited=[[[False]*(1<<k)for i in range(n)]for i in range(m)]
        queue=[]

        queue.append((startRow,startCol,0,0))
        visited[startRow][startCol][0] = True

        directions= [[-1,0],[0,1],[1,0],[0,-1]]

        while queue:
            row,col,steps,state = queue.pop(0)

            if state == ((1<<k)-1):
                return steps
            
            for r,c in directions:
                nr=row+r
                nc=col+c

                if nr<0 or nr>=m or nc<0 or nc>=n:
                    continue
                
                ch = grid[nr][nc]
                if ch == '#':
                    continue
                
                if ch>='A' and ch<='F':
                    if state & (1<<(ord(ch)-ord('A'))) == 0:
                        continue
                
                newState = state
                if ch>='a' and ch<='f':
                    newState |=(1<<(ord(ch)-ord('a')))
                
                if visited[nr][nc][newState]:
                    continue
                
                queue.append([nr,nc,steps+1,newState])
                visited[nr][nc][newState] = True
        return -1

        