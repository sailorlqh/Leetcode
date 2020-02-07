#using sling window to find the interval.
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if(k <= 1):
            return 0
        count = 0
        product = 1
        length = len(nums)
        left = right = 0
        for right in range(length):
            product *= nums[right]
            while(product >= k):
            	product /= nums[left]
            	left += 1
            count += right - left + 1
        return count

        
sol = Solution()
nums = [10, 5, 2, 6]
k = 100
print(sol.numSubarrayProductLessThanK(nums, k))