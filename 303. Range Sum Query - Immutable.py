class NumArray(object):
    dp = None
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        count = 0
        self.dp = [0 for i in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            count += nums[i-1]
            self.dp[i] = count
        print(self.dp)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1]-self.dp[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)