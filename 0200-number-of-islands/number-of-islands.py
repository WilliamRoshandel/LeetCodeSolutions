class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            if grid[i][j] != '1':
                return
            grid[i][j] = '0'

            if i > 0:
                dfs(i - 1, j)   #goes up a row: i + 1
            if i < rows - 1:
                dfs(i + 1, j)   #Check the row below: i - 1
            if j > 0:
                dfs(i, j - 1)
            if j < cols - 1:
                dfs(i, j + 1)
    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1

        return islands