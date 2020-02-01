class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
        	if(s[i-1] != '0'):
        		dp[i] = dp[i-1]
        	if(i >= 2):
        		temp = int(s[i-2:i])
        		if(temp >= 10 and temp <= 26):
        			dp[i] += dp[i-2]
      	return dp[-1]
        

sol = Solution()

a = "10"
print(sol.numDecodings(a))

#至少会有一种方法，所以dp[0]一定为1，用dp[i]来表示s[0:i]中存在的可能性。当各位上是0的时候，只有一种方法，当个位上不是0
#且数字在10～26之间的时候，会多一种拆分方式。也就是说，当个位上不是0的时候，dp[i]一定至少和dp[i-1]有一样多的方式
#当数字在10～26之间的时候，dp[i]还能加上dp[i-2]的方式，即dp[i-2]的拆分方式，在加上一个两位数。