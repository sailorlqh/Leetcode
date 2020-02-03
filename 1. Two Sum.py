class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = {}
        for i in range(len(nums)):
            com = target - nums[i]
            if(com in a):
                return [a[com], i]
            else:
                a[nums[i]] = i 
        