#this is a DP problem f(i，j) = f(i-1,j)+f(i,j-1)
#the first row and column is special, since once there is a obstacle in the row/column
#the points after the obstacle aren't reachable
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        x_flag = True
        y_flag = True
        for i in range(n):
            if(obstacleGrid[0][i] != 1 and x_flag):
                dp[0][i] = 1
            else:
                dp[0][i] = 0
                x_flag = False
        for i in range(m):
            if(obstacleGrid[i][0] != 1 and y_flag ):
                dp[i][0] = 1
            else:
                dp[i][0] = 0
                y_flag = False
        print(dp)
        for i in range(1,m,1):
            for j in range(1,n,1):
                if(obstacleGrid[i][j] == 1):
                    dp[i][j] = 0
                else:
                    dp[i][j] = 0
                    dp[i][j] += dp[i-1][j]
                    dp[i][j] += dp[i][j-1]
        print(dp)
        return dp[m-1][n-1]