class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 10000000000000000
        max_profit = 0
        for i in range(len(prices)):
            if(prices[i] < min_price):
                min_price = prices[i]
            elif(prices[i] - min_price > max_profit):
                max_profit = prices[i] - min_price
        return max_profit
sol = Solution()

a = [7,1,5,3,6,4]
# a = [2, 4, 1]
print(sol.maxProfit(a))