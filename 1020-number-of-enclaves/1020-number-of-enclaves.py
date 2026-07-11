class Solution(object):

    def numEnclaves(self, grid):

        rows = len(grid)
        cols = len(grid[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def dfs(row, col):

            if row < 0 or col < 0 or row >= rows or col >= cols:
                return

            if grid[row][col] == 0:
                return

            grid[row][col] = 0

            for dr, dc in directions:

                newRow = row + dr
                newCol = col + dc

                dfs(newRow, newCol)

        for i in range(rows):

            if grid[i][0] == 1:
                dfs(i, 0)

            if grid[i][cols - 1] == 1:
                dfs(i, cols - 1)

        for j in range(cols):

            if grid[0][j] == 1:
                dfs(0, j)

            if grid[rows - 1][j] == 1:
                dfs(rows - 1, j)

        count = 0

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:
                    count += 1

        return count