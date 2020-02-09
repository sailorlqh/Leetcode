class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid = [[0 for i in range(n)] for j in range(m)]
        island_set = []
        operation_nums = len(positions)
        if(operation_nums == 0):
        	return [0]
        count = [0 for i in range(operation_nums)]
        x = positions[0][0]
        y = positions[0][1]
        grid[x][y] += 1
        island_set.append([(x, y)])
        count[0] = 1
        # print(island_set)
        for i in range(1, operation_nums, 1):
        	# print_set(island_set)
        	# print('aaaaaa' + str(i))
        	x = positions[i][0]
        	y = positions[i][1]
        	if(grid[x][y] >= 1):
        		grid[x][y] += 1
        		count[i] = count[i-1]
        	else:
        		adj_positions = []
        		adj_count = 0
        		island_index = []
        		if(x - 1 >= 0 and grid[x-1][y] != 0):
        			adj_positions.append((x-1,y))
        			adj_count += 1
        		if(x + 1 < m and grid[x+1][y] != 0):
        			adj_positions.append((x+1, y))
        			adj_count += 1
        		if(y - 1 >= 0 and grid[x][y-1] != 0):
        			adj_positions.append((x,y-1))
        			adj_count += 1
        		if(y + 1 < n and grid[x][y+1] != 0):
        			adj_positions.append((x,y+1))
        			adj_count += 1
        		if(adj_count == 0):
        			island_set.append([(x,y)])
        			# count[i] = count[i-1]+1
        		else:
        			for j in range(len(island_set)):
        				for k in range(adj_count):
        					# print('-----')
        					# print(adj_positions[k])
        					if(adj_positions[k] in island_set[j] and j not in island_index):
        						island_index.append(j)
        			# print('adj_num: ' + str(len(island_index)))
        			if(len(island_index) == 1):
        				island_set[island_index[0]].append((x,y))
        				# count[i] = count[i-1]
        			else:
        				# count[i] = count[i-1]
        				island_set[island_index[0]].append((x,y))
        				for j in range(1, len(island_index)):
        					island_set[island_index[0]] += island_set[island_index[j]]
        					# count[i] -= 1
        				# print_set(island_set)
        				temp = []
        				for j in range(1, len(island_index)):
        					temp.append(island_set[island_index[j]])
        				for j in range(0, len(temp)):
        					# print('remove temp:')
        					# print(temp)
        					island_set.remove(temp[j])
        		count[i] = len(island_set)
        		grid[x][y] += 1
        	# print(count)
        return count


def print_set(a):
	print('print set:')
	length = len(a)
	for i in range(length):
		print(a[i])

sol = Solution()
m = 3
n = 3
positions = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
print(sol.numIslands2(m, n, positions))