# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#method one: using extra space to store each node in the list, and do it in one pass.
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        holder = []
        count = 0
        if(head.next == None):
            return None
        while(head != None):
            holder.append(head)
            count += 1
            head = head.next
        if(n == count):
            return curr.next
        elif(n == 1):
            holder[-2].next = None
        else:
            pos = count - n
            holder[pos-1].next = holder[pos+1]
        return curr

#method two: use two points to do it i  one pass.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = ListNode(0)
        curr.next = head
        pointer1 = curr
        pointer2 = curr
        for i in range(n+1):
            pointer1 = pointer1.next
        while pointer1 != None:
            pointer2 = pointer2.next
            pointer1 = pointer1.next
        pointer2.next = pointer2.next.next
        return curr.next
            
        
        
        
        