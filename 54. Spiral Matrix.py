class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        if(height != 0):
            width = len(matrix[0])
        else:
            return []
        count = 0
        ans = []
        new_count = 0
        while(new_count < height * width):
            # print(new_count)
            for i in range(count, width - count):
                ans.append(matrix[count][i])
                # print(1, matrix[count][i])
                new_count += 1
            for j in range(count + 1, height - count):
                # print(j, width - count)
                # print(2, matrix[j][width - count - 1])
                ans.append(matrix[j][width - count - 1])
                new_count += 1
            if(new_count >= height * width):
                break
            for i in range(width - count - 2, count - 1, -1):
                # print(3, matrix[height - count - 1][i])
                ans.append(matrix[height - count - 1][i])
                new_count += 1
            for j in range(height - 2 - count, count, -1):
                # print(4, matrix[j][count])
                ans.append(matrix[j][count])
                new_count += 1
            # print(ans)
            # print(new_count)
            # print('------')
            count += 1
        return ans
        