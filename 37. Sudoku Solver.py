class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.available_row = [[0 for i in range(10)] for j in range(9)]
        self.available_col = [[0 for i in range(10)] for j in range(9)]
        self.available_box = [[0 for i in range(10)] for j in range(9)]
        for i in range(9):
        	for j in range(9):
        		box_index = i / 3 * 3 + j/3
        		if(board[i][j] != '.'):
        			num = int(board[i][j])
        			self.available_row[i][num] = 1
        			self.available_col[j][num] = 1
        			self.available_box[box_index][num] = 1

        self.dfs(board)
    
    def dfs(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for char in '123456789':
                        num = int(char)
                        box_index = row / 3 * 3 + col / 3
                        if(self.available_row[row][num] == 0 and self.available_col[col][num] == 0 and self.available_box[box_index][num] == 0):
                        	self.available_row[row][num] = 1
                        	self.available_col[col][num] = 1
                        	self.available_box[box_index][num] = 1
                        	board[row][col] = char
                        	if(self.dfs(board)):
                        		return True
                        	else:
                        		self.available_row[row][num] = 0
                        		self.available_col[col][num] = 0
                        		self.available_box[box_index][num] = 0
                        		board[row][col] = '.'	

                    return False
        return True