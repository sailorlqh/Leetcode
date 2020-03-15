import heapq
class Solution:
	def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
		# class worker:
		# 	def __init__(self, a, b):
		# 		self.q = a
		# 		self.w = b
		# 		self.r = b/a
		# temp = []
		# for i in range(len(quality)):
		# 	temp.append(worker(quality[i], wage[i]))
		heap = []
		ans = 1000000000000000000000
		sortedWorker = sorted([w / q, q] for w, q in zip(wage, quality))
		sumQuality = 0
		for i in range(len(quality)):
			heapq.heappush(heap, -sortedWorker[i][1])
			sumQuality += sortedWorker[i][1]
			if(len(heap) > K):
				sumQuality += heapq.heappop(heap)
			if(len(heap) == K):
				ans = min(ans, sumQuality * sortedWorker[i][0])
		return ans
		