#version 1
#view this as a permutation problem, the result will be C(m+n-2)(n-1)
import math
class Solution(object):       
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return int(factoria(m+n-2)/(factoria(m-1)*factoria(n-1)))

def factoria(x):
    
    return math.factorial(x)

#version 2
#view this as a DP problem.

class Solution(object):       
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if(i == 0):
                    dp[i][j] = 1
                elif(j == 0):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
       