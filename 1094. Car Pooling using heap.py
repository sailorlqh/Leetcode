class Solution(object):
    def carPooling(self, trips, capacity):
        trips.sort(key=lambda x:x[1])
        cur = 0
        heap = []
        for a,b,c in trips:
            if not heap:
                heapq.heappush(heap, (c, a))
                cur += a
            else:
                while heap and heap[0][0] <= b:
                    cur -= heap[0][1]
                    heapq.heappop(heap)
                heapq.heappush(heap, (c, a))
                cur += a
            if cur > capacity:
                return False
        return True