class Solution(object):
    def func(self, x):
        return x[::-1]
    
    def is_overflow(self, x):
        print(x)
        temp = 2**31
        if(x > temp - 1 or x < -temp):
            print('fuck')
            return 0
        else:
            return x
        
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if(x[0] == '-'):
            return self.is_overflow(-1*int(self.func(x[1:])))
        else:
            return self.is_overflow(int(self.func(x)))
            
        