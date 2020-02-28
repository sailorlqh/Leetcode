class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_pos = None
        self.min_element = None
        
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) -  1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if(len(self.stack) != 0):
            return min(self.stack)
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()