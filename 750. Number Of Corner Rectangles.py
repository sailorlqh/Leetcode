class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        row = [[] for i in range(len(grid))]
        for i in range(len(grid)):
            temp = [0 for k in range(i)]
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    # print((i,j))
                    row[i].append(j)
                    for k in range(i):
                        if j in row[k]:
                            # print(haha)
                            temp[k] += 1
            for k in range(i):
                if(temp[k] == 0):
                    result += 0
                else:
                    result += (temp[k] * (temp[k]-1))/2
            # print(temp)
            # print('\n')
        # print(row)
        return result
                        
                    
            
grid = [[0,1,0],[1,0,1],[1,0,1],[0,1,0]]
sol = Solution()
print(sol.countCornerRectangles(grid))