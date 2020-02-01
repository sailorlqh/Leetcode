class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_a = len(s)
        len_b = len(p)
        dp = [[False for i in range(len_b+1)] for i in range(len_a+1)]
        dp[0][0] = True
        for i in range(2, len_b + 1):  #first letter can not be *
        	dp[0][i] = (p[i-1] == '*') and dp[0][i-2]
        for i in range(1, len_a+1):
        	for j in range(1, len_b+1):
        		if(p[j - 1] == '*'):
        			dp[i][j] = dp[i][j-2] or (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j] #* repeated for 0 times or 1 times or more times
        		else:
        			dp[i][j] = (p[j-1] == '.' or s[i-1] == p[j-1]) and dp[i-1][j-1]

        return dp[len_a][len_b]
        
s = "mississippi"
p = "mis*is*p*."

# s = "aab"
# p = "c*a*b"

sol = Solution()
print(sol.isMatch(s,p))