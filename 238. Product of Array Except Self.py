#when there is more than 1 zeros in the list
#all the result would be zero
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        nums_zero = nums.count(0)
        if nums_zero > 1:
            return [0] * length
        result = [0 for i in range(length)]
        result[0] = 1
        for i in range(1, length):
            result[i] = nums[i-1] * result[i-1]
        right_product = 1
        for j in range(length - 1, -1, -1):
            result[j] = result[j] * right_product
            right_product *= nums[j]
        return result
        