class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        lenth = len(nums)
        for i in range(len(nums)):
            if(i != 0 and nums[i] == nums[i-1]):
                continue
            j = i + 1
            k = len(nums)-1
            while(j < k):
                if(nums[i]+nums[j]+nums[k] == 0):
                    result.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1
                    while(j < k and nums[j-1] == nums[j]):
                        j = j + 1
                    while(k > j and nums[k+1] == nums[k]):
                        k = k - 1
                elif(nums[i]+nums[j]+nums[k] < 0):
                    j = j + 1
                elif(nums[i]+nums[j]+nums[k] > 0):
                    k = k - 1
        return result