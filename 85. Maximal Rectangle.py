class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        len_a = len(matrix)
        len_b = len(matrix[0])
        dp_row_max = [[-1 for i in range(len_b + 1)] for j in range(len_a )]
        dp_col_max = [[-1 for i in range(len_b)] for j in range(len_a + 1)]
        max_area = 0
        for i in range(len_a):
            for j in range(len_b):
                # print(i,j)
                if(int(matrix[i][j]) == 1):
                    if(dp_row_max[i][j] == -1):
                        dp_row_max[i][j+1] = 1
                    else:
                        dp_row_max[i][j+1] = dp_row_max[i][j]+1
                    if(dp_col_max[i][j] == -1):
                        dp_col_max[i+1][j] = 1
                    else:
                        dp_col_max[i+1][j] = dp_col_max[i][j] + 1
                    horizontal_len = min(dp_row_max[i][j+1], dp_row_max[i + 1- dp_col_max[i+1][j]][j+1])
                    # vertical_len = min(dp_col_max[i+1][j], dp_col_max[j + 1- dp_row_max[i][j+1]][j])
                    vertical_len = dp_col_max[i+1][j]
                    print(i, j, horizontal_len, vertical_len, vertical_len * horizontal_len)
                    max_area = max(horizontal_len * vertical_len, max_area)
        print(dp_row_max)
        print('\n')
        print(dp_col_max)
        return max_area

sol = Solution()
# a = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
a = [["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]
print(sol.maximalRectangle(a))