class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for x in range(col)]
        dp[0] = 1
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    if j > 0:
                        dp[j] += dp[j - 1]
        return dp[col - 1]
    # BFS Time Limit Exceeded
    # def uniquePathsWithObstacles(self, obstacleGrid):
    #     """
    #     :type obstacleGrid: List[List[int]]
    #     :rtype: int
    #     """
    #     row, col, count = len(obstacleGrid), len(obstacleGrid[0]), [0]
    #     if row == 1 and col == 1:
    #         if obstacleGrid[row - 1][col - 1] == 1:
    #             return 0
    #         elif obstacleGrid[row - 1][col - 1] == 0:
    #             return 1
    #
    #     visited = [[0 for x in range(col)] for x in range(row)]
    #
    #     def BFS(i, j, row, col, obstacleGrid, visited, count):
    #         if i < 0 or j < 0 or i >= row or j >= col:
    #             return
    #         if visited[i][j] == 1 or obstacleGrid[i][j] == 1:
    #             return
    #         if i + 1 == row and j + 1 == col:
    #             count[0] += 1
    #             return
    #         # count.append([i, j])
    #         visited[i][j] = 1
    #         BFS(i + 1, j, row, col, obstacleGrid, visited, count)
    #         # BFS(i - 1, j, row, col, obstacleGrid, visited, count)
    #         BFS(i, j + 1, row, col, obstacleGrid, visited, count)
    #         # BFS(i, j - 1, row, col, obstacleGrid, visited, count)
    #         visited[i][j] = 0
    #         # count.pop()
    #
    #     BFS(0, 0, row, col, obstacleGrid, visited, count)
    #     # return len(count)
    #     return count[0]


s = Solution()
grid = [[0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]]
print s.uniquePathsWithObstacles(grid)
