class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        fresh = 0
        q = []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        if fresh == 0:
            return 0
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        step = 0
        while q:
            size = len(q)
            for i in range(size):
                x, y = q.pop(0)
                for d in dirs:
                    nx, ny = x + d[0], y + d[1]
                    if nx < 0 or nx >= M or ny < 0 or ny >= N or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    q.append((nx, ny))
                    fresh -= 1
            step += 1
        if fresh != 0:
            return -1
        return step - 1