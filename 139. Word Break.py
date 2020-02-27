class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        if(length == 0):
            return True
        dp = [False for i in range(length+1)]
        dp[0] = True
        for i in range(1, length+1):
            for j in range(i):
                if(dp[j] and s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[-1]
        