class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if(len(intervals) == 0 or len(intervals) == 1):
            return len(intervals)
        new_intervals = sorted(intervals, key = lambda x:x[0])
        ans  = []
        ans.append(new_intervals[0])
        max_ans = 1
        for i in range(1, len(new_intervals)):
            flag = False
            for j in range(0, len(ans)):
                if(new_intervals[i][0] >= ans[j][1]):
                    flag = True
                    ans[j] = new_intervals[i]
                    break
            if(not flag):
                ans.append(new_intervals[i])
                max_ans += 1
        # print(ans)
        return max_ans
                    