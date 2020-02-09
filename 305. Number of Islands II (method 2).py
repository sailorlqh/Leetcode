class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """



sol = Solution()
m = 3
n = 3
positions = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
print(sol.numIslands2(m, n, positions))