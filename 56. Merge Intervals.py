class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals) == 0 or len(intervals) == 1):
            return intervals
        new_intervals = sorted(intervals, key = lambda x:x[0])
        print(new_intervals)
        ans = []
        ans.append(new_intervals[0])
        for i in range(1, len(new_intervals)):
            if(new_intervals[i][0] > ans[-1][1]):
                ans.append(new_intervals[i])
            else:
                if(new_intervals[i][1] > ans[-1][1]):
                    ans[-1][1] = new_intervals[i][1]
        return ans
        