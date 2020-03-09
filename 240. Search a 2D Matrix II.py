class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def helper(x1, y1, x2, y2):
            # print(x1, y1, x2, y2)
            if(x1 >= len(matrix) or y1 >= len(matrix[0]) or x2 >= len(matrix) or y2 >= len(matrix[0]) or x1 < 0 or y1 < 0 or x1 > x2 or y1 > y2):
                return False
            if(x1 == x2 and y1 == y2):
                return matrix[x1][y1] == target

            mid_x = (x1 + x2)//2
            mid_y = (y1 + y2)//2
            # print(mid_x, mid_y)

            if(mid_x >= len(matrix) or mid_y >= len(matrix[0])):
                return False
            if(matrix[mid_x][mid_y] == target):
                return True
            if(matrix[mid_x][mid_y] > target):
                return helper(x1, y1, mid_x, mid_y) or helper(x1, mid_y+1, mid_x, y2) or helper(mid_x + 1, y1, x2, mid_y)
            else:
                return helper(x1, mid_y+1, mid_x, y2) or helper(mid_x + 1, y1, x2, y2)
        if(len(matrix) == 0):
            return False
        if(len(matrix[0]) == 0):
            return False
        return helper(0,0,len(matrix)-1, len(matrix[0]) - 1)