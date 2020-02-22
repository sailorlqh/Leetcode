from collections import OrderedDict
class LRUCache:

    max_capacity = None
    a = None
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.a = OrderedDict()
        self.max_capacity = capacity
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if(key in self.a.keys()):
            self.a.move_to_end(key)
            
            return self.a[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if(key in self.a.keys()):
            self.a.move_to_end(key)
        self.a[key] = value
        if(len(self.a) > self.max_capacity):
            self.a.popitem(last = False)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)