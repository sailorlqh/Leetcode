#DP problem
#version 1:
#use another 2-D array
class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		len_x = len(grid)
		len_y = len(grid[0])
		pathSum = [[0 for i in range(len_y)] for j in range(len_x)]
		# pathSum[0][0] = grid[0][0]
		# print(pathSum)
		for i in range(len_x):
			for j in range(len_y):
				if(i == 0 and j == 0):
					pathSum[i][j] = grid[i][j]
				elif(i == 0):
					pathSum[i][j] = pathSum[i][j-1]+grid[i][j]
				elif(j == 0):
					pathSum[i][j] = pathSum[i-1][j] + grid[i][j]
				else:
					pathSum[i][j] = min(pathSum[i-1][j]+grid[i][j], pathSum[i][j-1]+grid[i][j])

		return pathSum[len_x-1][len_y-1]

#version two
#simply operate on grid
class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		len_x = len(grid)
		len_y = len(grid[0])
		# pathSum = [[0 for i in range(len_y)] for j in range(len_x)]
		# pathSum[0][0] = grid[0][0]
		# print(pathSum)
		for i in range(len_x):
			for j in range(len_y):
				if(i == 0 and j == 0):
					continue
				elif(i == 0):
					grid[i][j] = grid[i][j-1]+grid[i][j]
				elif(j == 0):
					grid[i][j] = grid[i-1][j] + grid[i][j]
				else:
					grid[i][j] = min(grid[i-1][j]+grid[i][j], grid[i][j-1]+grid[i][j])

		return grid[len_x-1][len_y-1]
