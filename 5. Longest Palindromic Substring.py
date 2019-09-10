#version 1: use DP to solve
#Runtime 4404ms > 23.18%
#Memory: 20.5.  < 10.96%
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lenth = len(s)
        dp_arr = [[0 for i in range(lenth)] for j in range(lenth)]
        left = 0
        right = 0
        max_lenth = 1
        for i in range(lenth):
            dp_arr[i][i] = 1
            for j in range(i):
                if(s[i] == s[j] and (i - j < 2 or dp_arr[j+1][i-1] == 1)):
                    dp_arr[j][i] = 1
                if(dp_arr[j][i] == 1 and max_lenth < i - j + 1):
                    max_lenth = i - j + 1
                    left = j
        return s[left:left+max_lenth]