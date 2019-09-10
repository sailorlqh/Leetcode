class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        first_row_flag = False
        for j in range(num_cols):
            if(matrix[0][j] == 0):
                first_row_flag = True
        for i in range(1, num_rows):
            for j in range(num_cols):
                if(matrix[i][j] == 0):
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, num_rows):
            for j in range(num_cols-1,-1,-1):
                if(matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
                    
        if first_row_flag == True:
            for j in range(num_cols):
                matrix[0][j] = 0
# the key point to this question is that the [0][0] can only be used to flag first row or first col
#the other one will need another variable to set flag.
#as we use [0][0] to determine first col, than first_row_flag is used to determine first row
#once we set the first_row_flag, we skip first row when marking and operate the first row when evetything
#else is done