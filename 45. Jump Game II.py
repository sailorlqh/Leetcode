#Treat is as some intervals, and for each interval, we try to find the maximum position we can reach.
#and the position can be treated as the start of the next interval
#last_pos is the start of some interval, 
#max_pos in the maximum position we can reach via a point in the interval
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        ans = 0
        max_pos = 0
        last_pos = 0
        for i in range(length - 1):
            max_pos = max(max_pos, nums[i] + i)
            if(i == last_pos):
                last_pos = max_pos
                ans += 1
                if(last_pos >= length - 1):
                    return ans
        return ans