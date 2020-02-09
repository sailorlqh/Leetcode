#use dfs and set each searched point to 0
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """       
        m = len(grid)
        if(m == 0):
            return 0
        n = len(grid[0])
        count = 0
        queue_x = []
        queue_y = []
        for i in range(m):
            for j in range(n):
                # print(i, j, grid[i][j])
                if(grid[i][j] == '1'):
                    # print('fuck')
                    grid[i][j] = '0'
                    if(i + 1 < m and grid[i+1][j] == '1'):
                        queue_x.append(i+1)
                        queue_y.append(j)
                    if(i - 1 >= 0 and grid[i-1][j] =='1'):
                        queue_x.append(i-1)
                        queue_y.append(j)
                    if(j + 1 < n and grid[i][j+1] == '1'):
                        queue_x.append(i)
                        queue_y.append(j+1)
                    if(j - 1 >= 0 and grid[i][j-1] == '1'):
                        queue_x.append(i)
                        queue_y.append(j-1)
                    while(len(queue_x) != 0):
                        x = queue_x.pop()
                        y = queue_y.pop()
                        grid[x][y] = '0'
                        if(x + 1 < m and grid[x+1][y] == '1'):
                            queue_x.append(x+1)
                            queue_y.append(y)
                        if(x - 1 >= 0 and grid[x-1][y] =='1'):
                            queue_x.append(x-1)
                            queue_y.append(y)
                        if(y + 1 < n and grid[x][y+1] == '1'):
                            queue_x.append(x)
                            queue_y.append(y+1)
                        if(y - 1 >= 0 and grid[x][y-1] == '1'):
                            queue_x.append(x)
                            queue_y.append(y-1)
                    # print_grid(grid)
                    count += 1
        return count
                    
def print_grid(a):
    for i in range(len(a)):
        print(a[i])
    print('\n')

sol = Solution()
# a = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
a = [["1","1","1"],["0","1","0"],["1","1","1"]]
print_grid(a)
# 11000
# 00100
# 00011
print(sol.numIslands(a))