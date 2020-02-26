class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        new_intervals = sorted(intervals, key = lambda x:x[0])
        for i in range(1, len(new_intervals)):
            if(new_intervals[i][0] < new_intervals[i-1][1]):
                return False
        return True
        