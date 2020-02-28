class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_dict = [{}for i in range(9)]
        col_dict = [{}for i in range(9)]
        box_dict = [{}for i in range(9)]
        for i in range(9):
            for j in range(9):
                if(board[i][j] != '.'):
                    num = int(board[i][j])
                    if(num in row_dict[j].keys()):
                        return False
                    else:
                        row_dict[j][num] = 1
                    if(num in col_dict[i].keys()):
                        print(col_dict[i])
                        return False
                    else:
                        col_dict[i][num] = 1
                    box_index = i / 3 * 3 + j / 3
                    if(num in box_dict[box_index].keys()):
                        return False
                    else:
                        box_dict[box_index][num] = 1
        return True
        