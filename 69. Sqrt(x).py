from math import e, log
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 1:
            return 0
        if x < 2:
            return 1
        lower_bound = int(e**(0.5 * log(x)))
        upper_bound = lower_bound + 1
        if(upper_bound ** 2) > x:
            return lower_bound
        else:
            return upper_bound
        