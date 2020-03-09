class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x1 = 0
        y1 = 0
        x2 = len(matrix) - 1
        if(x2 != -1):
            y2 = len(matrix[0]) - 1
            if(y2 == -1):
                return False
        else:
            return False
        if(target < matrix[0][0] or target > matrix[x2][y2]):
            return False
        selectedRow = None
        while(True):
            if(x1 > x2):
                return False
            if(x1 == x2):
                selectedRow = x1
                break
            mid = (x1 + x2)//2
            print(matrix[mid][-1])
            if(matrix[mid][-1] > target):
                if(mid == 0 or matrix[mid-1][-1] < target):
                    selectedRow = mid
                    break
                elif(matrix[mid-1][-1] == target):
                    return True
                else:
                    x2 = mid-1
            elif(matrix[mid][-1] == target):
                return True
            else:
                if(mid + 1 < len(matrix)):
                    x1 = mid+1
                else:
                    selectedRow = mid
                    break
        while(True):
            print(matrix[selectedRow])
            if(y1 > y2):
                return False
            if(y1 == y2):
                return matrix[selectedRow][y1] == target
            mid = (y1 + y2)//2
            if(matrix[selectedRow][mid] == target):
                return True
            elif(matrix[selectedRow][mid] < target):
                y1 = mid + 1
            else:
                y2 = mid - 1