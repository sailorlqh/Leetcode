class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if (n == 1):
            return int(1)
        else:
            dp = [0 for i in range(n+1)]
            dp[0] = 1
            for i in range(1, n+1):
                dp[i] = dp[i-1]+dp[i-2]
            return dp[-1]
        