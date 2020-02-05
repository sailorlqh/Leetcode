class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_num = len(nums)
        # max_values = []
        # min_values = []
        max_values = [0 for i in range(len_num)]
        min_values = [0 for j in range(len_num)]
        # max_values.append(nums[0])
        # min_values.append(nums[0])
        max_values[0] = nums[0]
        min_values[0] = nums[0]
        result = nums[0]
        # print(result)
        for i in range(1, len_num):
        	temp1 = max_values[i - 1] * nums[i]
        	temp2 = min_values[i - 1] * nums[i]
        	# print(temp1, temp2)
        	max_values[i] = (max(temp1, temp2, nums[i]))
        	min_values[i] = (min(temp1, temp2, nums[i]))
        	result = max(result, max_values[i])
        return result
        

sol = Solution()
# a = [2,3,-2,4]
a = [-2,0,-1]
print(sol.maxProduct(a))
