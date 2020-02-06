class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        dp = []
        dp.append(-1)
        lenth = len(heights)
        for i in range(lenth):
            while(dp[len(dp) - 1] != -1 and heights[dp[len(dp) - 1]] >= heights[i]):
                max_area = max(max_area, heights[dp.pop()] * (i - dp[len(dp) - 1] -1))   
            dp.append(i)
        while(dp[len(dp) - 1] != -1):
            max_area = max(max_area, heights[dp.pop()] * (lenth - dp[len(dp) - 1] - 1))
        return max_area
               