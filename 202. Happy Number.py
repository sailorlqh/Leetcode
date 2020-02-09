class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def next_num(n):
            total = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total += digit ** 2
            return total
        
        if(n <= 0):
            return False
        result = set()
        while n != 1 and n not in result:
            result.add(n)
            n = next_num(n)
        return n == 1
        
        
        