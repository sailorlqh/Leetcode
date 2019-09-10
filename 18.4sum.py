class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        lenth = len(nums)
        result = set()
        for i in range(lenth):
            j = i + 1
            while(j < lenth - 2):
                k = j + 1
                l = lenth -1
                while(k < l):
                    temp = nums[i] + nums[j] + nums[k] + nums[l]
                    if(temp == target):
                        result.add((nums[i], nums[j], nums[k], nums[l]))
                        k = k + 1
                        l = l - 1
                    elif(temp < target):
                        k = k + 1
                    elif(temp > target):
                        l = l - 1
                j = j + 1
        return list(result)