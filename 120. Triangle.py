class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # def print()
        height = len(triangle)
        if(height == 0):
            return 0
        for i in range(1, height):
            for j in range(len(triangle[i])):
                if(j == 0):
                    triangle[i][j] += triangle[i-1][j]
                elif(j == i):
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[height-1])
                    
        