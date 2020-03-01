class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        temp_count = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                temp_count += 1
            elif(nums[i] == 0):
                max_count = max(temp_count, max_count);
                temp_count = 0
        return max(max_count, temp_count);
                
            
        