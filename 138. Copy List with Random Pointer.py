"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#use hash table to store the node that has already been visited
#and when the next_node or random_node is in the table, copy it
#or build a new node
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        new_list = []
        random_list = []
        curr = None
        a = {}
        if(head == None):
            return None
        curr = Node(head.val)
        a[head] = curr
        new_head = Node(0)
        new_head.next = curr
        while(head != None):
            val = head.val
            next_node = head.next
            random_node = head.random
            if(next_node != None):
                if(next_node not in a):
                    new_node = Node(next_node.val)
                    curr.next = new_node
                    a[next_node] = new_node
                else:
                    curr.next = a[next_node]
            if(random_node != None):
                if(random_node != None and random_node not in a):
                    new_node = Node(random_node.val)
                    curr.random = new_node
                    a[random_node] = new_node
                else:
                    curr.random = a[random_node]
            head = head.next
            curr = curr.next
        return new_head.next
