class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        max_num = nums[0]
        for i in range(1, size):
        	if(nums[i-1]) >= 0:
        		nums[i] += nums[i-1]
        	max_num = max(nums[i], max_num)
        return max_num

sol = Solution()

a = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(a))