import heapq
class Solution:
	def maxPerformance(self, n, speed, efficiency, k):
		class engineer():
			def __init__(self, a, b):
				self.speed = a
				self.efficiency = b
		heapq
		temp = []
		h = []
		sumSpeed = 0
		res = 0
		for i in range(n):
			temp.append(engineer(speed[i], efficiency[i]))
		sortedEngineer = sorted(temp, key = lambda x: x.efficiency, reverse = 1)
		for i in range(n):
			heapq.heappush(h, sortedEngineer[i].speed)
			sumSpeed += sortedEngineer[i].speed
			if(len(h) > k):
				sumSpeed -= heapq.heappop(h)
			res = max(res, sumSpeed * sortedEngineer[i].efficiency)
		return res
sol = Solution()
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
print(sol.maxPerformance(n, speed, efficiency, k))