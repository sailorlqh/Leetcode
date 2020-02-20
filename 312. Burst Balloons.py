#using DP to solve this proble
#instead of killing ballons one by one
#we can add a ballon one by one
#i.e. the reverse of killing all ballons
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        nums.insert(length, 1)
        nums.insert(0,1)
        dp = [[0] * (length + 2) for i in range(length + 2)]

        for temp_length in range(1, length+1):
        	for i in range(1, length - temp_length+2):
        		j = i + temp_length - 1
        		dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[k]*nums[i-1]*nums[j+1] for k in range(i, j+1))
        return dp[1][length]