#update another method to solve this problem
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #using dp to solve this problem
        #run time : (N^2)
        len_s = len(s)
        len_p = len(p)
        if(len_s == len_p and len_s == 0):
            return True
        elif(len_p == 0):
            return False
        dp = [[False for i in range(len_s + 1)] for j in range(len_p + 1)]
        # print(dp)
        dp[0][0] = True
        # print(dp)
        if(p[0] == '*'):
        	dp[1][0] = True
        	for i in range(len_s+1):
        		dp[0][i] = True
        for i in range(1, len_p+1):
        	for j in range(1, len_s + 1):
        		if(p[i-1] == '*'):
        			if(i != len_p):
        				dp[i][0] = dp[i-1][0]
        				dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
        			else:
        				dp[i][j] = dp[i-1][j] or dp[i][j-1]
        		else:
        			dp[i][j] = (p[i-1] == s[j-1] or p[i-1] == '?') and dp[i-1][j-1]

        return dp[-1][-1]

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #a better solution than using dp
        #This solution have run time: n
        len_s = len(s)
        len_p = len(p)
        s_ptr = 0
        p_ptr = 0
        temp_s_ptr = -1
        star_ptr = -1
        while s_ptr < len_s:
        	if(p_ptr < len_p and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr])):
        		p_ptr += 1
        		s_ptr += 1
        	elif(p_ptr < len_p and p[p_ptr] == '*'):
        		star_ptr = p_ptr
        		temp_s_ptr = s_ptr
        		p_ptr += 1
        	elif(star_ptr == -1):
        		return False
        	else:
        		p_ptr = star_ptr + 1
        		s_ptr = temp_s_ptr + 1
        		temp_s_ptr = s_ptr
        return all(x == '*' for x in p[p_ptr:])




sol = Solution()
s = "ab"
p = "*?*?*"
s = 'ho'
p = '**ho'
s = 'aab'
p = 'c*a*b'
print(sol.isMatch(s, p))