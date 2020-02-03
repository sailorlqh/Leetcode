class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        answer = [[0 for i in range(n)] for j in range(m)]
        # dp[0][0] = mat[0][0]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + mat[i][j]
        for i in range(m):
            for j in range(n):
                x1 = max(0, j - k)
                x2 = min(n, j + k+1)
                y1 = max(0, i - k)
                y2 = min(m, i + k+1)
                answer[i][j] = dp[y2][x2] - dp[y2][x1] - dp[y1][x2] + dp[y1][x1]
        return answer




sol = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
K = 1
sol.matrixBlockSum(mat, K)
# print(sol.matrixBlockSum(mat, K))