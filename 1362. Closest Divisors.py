import math
class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        def find_divier(num):
            min_diff = 1000000000
            temp = int(math.sqrt(num))
            ans = []
            temp += 1
            for i in range(1, temp + 1):
                if(num % i == 0):
                    temp1 = num / i
                    temp = abs(num / i - i)
                    if(min_diff > temp):
                        ans = [i, temp1]
                        min_diff = temp
                    # min_diff = min(min_diff, abs(num / i - i))
            return ans, min_diff
        ans1, diff1 = find_divier(num+1)
        ans2, diff2 = find_divier(num+2)
        return ans1 if diff1 < diff2 else ans2
        