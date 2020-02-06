#solution is 5 = 4 + 1 = dp[4] + dp[1] ('100' + '1')
#whenever n is the 2^n, there will only be one '1'
#use base1 to store lower bound of power and base2 to store the upper bound of power
#instead of calculate the power each time, store them will make the program faster
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if(num == 0):
            return [0]
        dp = [0 for i in range(num + 1)]
        dp[0] = 0
        dp[1] = 1
        power = 0
        base1 = 2**(power)
        base2 = 2**(power+1)
        for i in range(2, num + 1):
            if(i == base2):
                # print('aaaa')
                dp[i] = 1
                power += 1
                base1 = base2
                base2 = 2**(power + 1)
                # print(dp)
            else:
                dp[i] = 1 + dp[i - base1]
        return dp
        
sol = Solution()
print(sol.countBits(5))