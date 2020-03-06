class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n)]
        dp[0] = 1
        ptr2 = 0
        ptr3 = 0
        ptr5 = 0
        for i in range(1, n):
            ugly = min(dp[ptr2] * 2, dp[ptr3] * 3, dp[ptr5] * 5)
            dp[i] = ugly
            
            if(ugly == dp[ptr2] * 2):
                ptr2 += 1
            if(ugly == dp[ptr3] * 3):
                ptr3 += 1
            if(ugly == dp[ptr5] * 5):
                ptr5 += 1
        return dp[-1]
        
        