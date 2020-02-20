class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a = {}
        length = len(nums)
        max_length = 0
        count = 0
        for i in range(length):
            count += nums[i]
            if(count == k):
                max_length = i+1
            elif(count - k in a):
                max_length = max(max_length, i - a[count - k])
            if(count not in a):
                a[count] = i
        return max_length