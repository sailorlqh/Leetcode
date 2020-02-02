class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if(len(costs) == 0):
            return 0
        if(len(costs) == 1):
            return min(costs[0])
        else:
            dp = costs
            for i in range(len(dp)-2, -1, -1):
                for j in range(0, 3):
                    temp = dp[i+1][0:j]+dp[i+1][j+1:]
                    dp[i][j] = dp[i][j]+min(temp)
            return min(dp[0])
            