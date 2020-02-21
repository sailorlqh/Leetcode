#Quite like a DP question, but using greedy is faster
#if a point is reachable, set value to 1
#and check whether the end can be reached
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        leftIndex = length - 1
        dp = [-1 for i in range(length)]
        for i in range(length - 1, -1, -1):
            if(i + nums[i] >= leftIndex):
                leftIndex = i
        return leftIndex == 0

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        if(length == 1):
            return True
        leftIndex = nums[0]
        for i in range(1, length):
            if(i <= leftIndex):
                leftIndex = max(i + nums[i], leftIndex)
        return leftIndex >= length - 1