class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        height = len(word1)
        width = len(word2)
        if(height == 0):
            return width
        if(width == 0):
            return height
        dp = [[0 for i in range(width+1)] for j in range(height+1)]
        for i in range(height+1):
            for j in range(width + 1):
                if(i == 0):
                    dp[i][j] = j
                elif(j == 0):
                    dp[i][j] = i
                else:
                    top = dp[i-1][j]
                    left = dp[i][j-1]
                    top_left = dp[i-1][j-1]
                    if(word1[i-1] == word2[j-1]):
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(top, left, top_left)
        return dp[-1][-1]