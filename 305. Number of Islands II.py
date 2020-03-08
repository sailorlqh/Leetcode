class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        numOp = len(positions)
        if(numOp == 0 or (m == 0 and n==0)):
            return [0]
        islandMap = [[0 for i in range(n)] for j in range(m)]
        union = {}
        union[1] = [positions[0]]
        islandMap[positions[0][0]][positions[0][1]] = 1
        ans = [1]
        # print(union)
        count = 1
        for i in range(1, numOp):
            op = positions[i]
            [x, y] = op
            if(islandMap[x][y] >= 1):
                ans.append(len(union))
                continue;

            neighbor = []
            if(x-1 >= 0):
                neighbor.append([x-1, y])
            if(y-1 >= 0):
                neighbor.append([x, y-1])
            if(x + 1 < m):
                neighbor.append([x+1, y])
            if(y + 1 < n):
                neighbor.append([x, y+1])
            possibleKeys = set()
            # print(neighbor)
            for j in range(len(neighbor)):
                if(islandMap[neighbor[j][0]][neighbor[j][1]] >= 1):
                    possibleKeys.add(islandMap[neighbor[j][0]][neighbor[j][1]])
            # print(len(possibleKeys))
            if(len(possibleKeys) != 0):
                temp_count = 0
                merge_element = None;
                for element in possibleKeys:
                    if(temp_count == 0):
                        union[element].append(op)
                        islandMap[x][y] = element
                        merge_element = element
                    else:
                        union[merge_element] += union[element]
                        for pos in union[element]:
                            islandMap[pos[0]][pos[1]] = merge_element
                        union.pop(element)
                    temp_count += 1
            else:
                count += 1
                union[count] = [op]
                islandMap[op[0]][op[1]] = count
            # print(union)
            ans.append(len(union))
        return ans