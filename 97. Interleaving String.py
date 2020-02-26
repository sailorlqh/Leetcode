from collections import Counter
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        a = Counter(s1+s2)
        c = Counter(s3)
        if(a != c):
            return False
        height = len(s1)
        width = len(s2)
        total = len(s3)
        dp = [[False for i in range(width + 1)] for j in range(height + 1)]
        for i in range(height+1):
            for j in range(width+1):
                if(i == 0 and j == 0):
                    dp[0][0] = True
                elif(i == 0):
                    dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
                elif(j == 0):
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i+j-1]
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        # print(dp)
        return dp[-1][-1]