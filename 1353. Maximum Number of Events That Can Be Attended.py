class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key = lambda x:x[1])
        length = len(events)
        occupied_date = set()
        ans = 0
        for i in range(length):
            for j in range(events[i][0], events[i][1] + 1):
                if(j not in occupied_date):
                    ans += 1
                    occupied_date.add(j)
                    break
        return ans