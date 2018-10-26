# https://leetcode.com/problems/minimum-path-sum/
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        dp = [[0 for x in range(col)] for y in range(row)]
        dp[0][0] = grid[0][0]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j - 1] + grid[i][j], dp[i - 1][j] + grid[i][j])
            # print dp
        return dp[row - 1][col - 1]


s = Solution()
grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]
print s.minPathSum(grid)
