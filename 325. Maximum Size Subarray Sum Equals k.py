class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_length = 0
        left = 0
        right = 0
        current_sum = 0
        sum_positive = 0
        sum_negative = 0
        length = len(nums)
        for right in range(length):
        	current_sum = sum_negative + sum_positive + nums[right]
        	while(current_sum > k):
        		# current_sum -= nums[left]
        		if(nums[left] >= 0):
        			sum_positive -= nums[left]
        		else:
        			sum_negative -= nums[left]
        		left += 1
        		current_sum = sum_negative + sum_positive + nums[right]
        	if(nums[right] >= 0):
        		sum_positive += nums[right]
        	else:
        		sum_negative += nums[right]
        	current_sum = sum_positive + sum_negative
        	if(current_sum == k):
        		max_length = max(max_length, right - left + 1)
        return max_length

sol = Solution()
nums = [1, -1, 5, -2, 3]
k = 3
print(sol.maxSubArrayLen(nums, k))