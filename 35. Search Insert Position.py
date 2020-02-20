class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(left, right):
            while(left < right):
                mid = (left + right) / 2
            # print(left, right, mid, nums[mid])
                if(nums[mid] < target and nums[mid+1] > target):
                    return mid+1
                elif(nums[mid] < target):
                    left = mid
                else:
                    right = mid               
        if target in nums:
            return nums.index(target)
        length = len(nums)
        if(target < nums[0]):
            return 0
        if(target > nums[-1]):
            return length
        return helper(0, length)
        