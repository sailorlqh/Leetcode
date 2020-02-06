class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        dp = []
        dp.append(-1)
        lenth = len(heights)
        for i in range(lenth):
            while(dp[len(dp) - 1] != -1 and heights[dp[len(dp) - 1]] >= heights[i]):
                max_area = max(max_area, heights[dp.pop()] * (i - dp[len(dp) - 1] -1))   
            dp.append(i)
        while(dp[len(dp) - 1] != -1):
            max_area = max(max_area, heights[dp.pop()] * (lenth - dp[len(dp) - 1] - 1))
        return max_area

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
                    # if(dp_row_max[i][j] == -1):
                    #     dp_row_max[i][j+1] = 1
                    # else:
                    #     dp_row_max[i][j+1] = dp_row_max[i][j]+1
                    if(dp_col_max[i][j] == -1):
                        dp_col_max[i+1][j] = 1
                    else:
                        dp_col_max[i+1][j] = dp_col_max[i][j] + 1
            max_area = max(self.largestRectangleArea(dp_col_max[i+1]), max_area)
                    # horizontal_len = min(dp_row_max[i][j+1], dp_row_max[i + 1- dp_col_max[i+1][j]][j+1])
                    # # vertical_len = min(dp_col_max[i+1][j], dp_col_max[j + 1- dp_row_max[i][j+1]][j])
                    # vertical_len = dp_col_max[i+1][j]
                    # if(vertical_len = dp_col_max[i+1 - ])
                    # print(i, j, horizontal_len, vertical_len, vertical_len * horizontal_len)
                    # max_area = max(horizontal_len * vertical_len, max_area)

        # print(dp_row_max)
        # print('\n')
        # print(dp_col_max)
        return max_area

sol = Solution()
# a = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
a = [["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]
print(sol.maximalRectangle(a))