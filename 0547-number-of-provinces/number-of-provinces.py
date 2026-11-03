class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        count = 0
        visited = [False] * n

        def dfs(i):
            visited[i] = True
            for j in range(n):
                if visited[j] == False and isConnected[i][j] == 1:
                    dfs(j)

            

        for i in range(n):
            if visited[i] != True:
                dfs(i)
                count += 1

        return count
