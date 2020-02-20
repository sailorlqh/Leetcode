class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        index = nums.index(target)
        temp = index
        while(nums[temp] == target):
            temp += 1
            if(temp == len(nums)):
                break
        return [index, temp-1]
        