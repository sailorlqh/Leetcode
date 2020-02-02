class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if(len(cost) == 0):
            return 0
        if(len(cost) == 1):
            return cost[0]
        if(len(cost) == 2):
            return min(cost)
        dp = [0 for i in range(len(cost)+1)]
        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1]+cost[i-1])
        return dp[-1]
        