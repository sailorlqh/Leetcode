class CustomStack:

    def __init__(self, maxSize: int):
    	self.maxSize = maxSize
    	self.stack = []
        

    def push(self, x: int) -> None:
        if(len(self.stack) < self.maxSize):
        	self.stack.append(x)

    def pop(self) -> int:
    	if(len(self.stack) != 0):
    		return self.stack.pop()
    	else:
    		return -1
        

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
        	if(i >= len(self.stack)):
        		break
        	else:
        		self.stack[i] += val