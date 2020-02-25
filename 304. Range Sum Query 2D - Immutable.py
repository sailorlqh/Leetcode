class NumMatrix(object):
    dp = None
    answer = None
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        mat = matrix
        m = len(matrix)
        if(m == 0):
            dp = []
            return
        n = len(matrix[0])
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        answer = [[0 for i in range(n)] for j in range(m)]
        # dp[0][0] = mat[0][0]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + mat[i][j]
        self.dp = dp
        # print(self.dp)
                
        
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if self.dp == None:
            return None
        else:
            return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)