class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i = 1
        while(i < length):
            if(i >= length):
                return len(nums)
            if(nums[i] == nums[i-1]):
                nums.pop(i)
                i = i - 1
                length = len(nums)
            i += 1
        