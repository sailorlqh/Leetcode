
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [0 for i in range(length)]
        result[0] = 1
        for i in range(1, length):
            result[i] = nums[i-1] * result[i-1]
        right_product = 1
        for j in range(length - 1, -1, -1):
            result[j] = result[j] * right_product
            right_product *= nums[j]
        return result
        