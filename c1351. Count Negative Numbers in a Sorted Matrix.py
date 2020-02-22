class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length_row = len(grid)
        if(length_row == 0):
            return 0
        length_col = len(grid[0])
        if(length_col == 0):
            return 0
        ans = 0
        i = 0
        j = 0
        while(i < length_row):
            # print('i: ', i)
            j = 0
            while(j < length_col):
                if(grid[i][j] < 0):
                    ans += length_col - j
                    # i += 1
                    # print(ans)
                    break
                j += 1
            i += 1
        return ans