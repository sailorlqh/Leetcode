class ProductOfNumbers(object):
    prod = None
    length = None
    nums = None
    curr_prod = None
    right_most_zero = None
    
    def __init__(self):
        self.prod = []
        self.length = 0
        self.nums = []
        self.curr_prod = 1
        self.prod.append(1)
        self.right_most_zero = -1
        

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        # self.nums.append(num)
        self.curr_prod *= num
        if(num == 0):
            self.curr_prod = 1
            self.right_most_zero = self.length
        self.prod.append(self.curr_prod)
        self.length += 1
        
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if(self.length - k - 1< self.right_most_zero):
            return 0
        else:
            temp = self.curr_prod / self.prod[- k - 1]
            return temp