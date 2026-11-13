class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if grid[i][j] != '1':
                return
            grid[i][j] = '0'

            if i > 0:
                dfs(i - 1, j)
            if i < rows - 1:
                dfs(i + 1, j)
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

