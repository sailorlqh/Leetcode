class Solution:
	def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
		height = len(matrix)
		width = len(matrix[0])
		ans = []
		dpRow = [[-1 for i in range(width)] for j in range(height)]
		dpCol = [[-1 for i in range(width)] for j in range(height)]
		for i in range(height):
			for j in range(width):
				if(i == 0):
					dpCol[i][j] = 0
				elif(matrix[i][j] > matrix[dpCol[i-1][j]][j]):
					dpCol[i][j] = i
				else:
					dpCol[i][j] = dpCol[i-1][j]

				if(j == 0):
					dpRow[i][j] = 0
				elif(matrix[i][j] < matrix[i][dpRow[i][j-1]]):
					dpRow[i][j] = j
				else:
					dpRow[i][j] = dpRow[i][j-1]

		print(dpCol)
		print(dpRow)
		for i in range(height):
			colNum = dpRow[i][-1]
			if(dpCol[-1][colNum] == i):
				ans.append(matrix[i][colNum])
		return ans