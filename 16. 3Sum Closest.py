class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        length = len(nums)
        for i in range(length):
            j = i + 1
            k = length - 1
            while j < k:
                # print(i, j, k)
                temp_result = nums[i] + nums[j] + nums[k]
                if(abs(temp_result - target) < abs(result - target)):
                    result = temp_result
                if(temp_result < target):
                    j = j + 1
                elif(temp_result > target):
                    k = k - 1
                else:
                    return temp_result
        return result