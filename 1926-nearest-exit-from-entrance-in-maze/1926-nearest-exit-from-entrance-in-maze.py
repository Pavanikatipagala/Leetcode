class Solution(object):
    def nearestExit(self, maze, entrance):
        m = len(maze)
        n = len(maze[0])

        startRow =entrance[0]
        startCol = entrance[1]

        queue = deque()
        queue.append((startRow,startCol,0))
        maze[startRow][startCol] = '+'

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            r,c,dist = queue.popleft()

            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                
                if nr<0 or nr>m-1 or nc<0 or nc>n-1 or maze[nr][nc] == '+':
                    continue
                
                if nr==0 or nr==m-1 or nc==0 or nc==n-1:
                    return dist+1

                maze[nr][nc] ='+'
                queue.append((nr,nc,dist+1))
        return -1                
                

