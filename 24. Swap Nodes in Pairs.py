# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def swap(curr):
            temp = curr
            temp2 = curr.next.next
            curr = curr.next
            curr.next = temp
            temp.next = temp2
            return curr
        
        if(head == None):
            return None
        if(head.next == None):
            return head
        prev = ListNode(0)
        newHead = prev
        curr = head
        while(curr != None and curr.next != None):
            prev.next = swap(curr)
            curr = curr.next
            prev = prev.next.next
        return newHead.next
        
        
        
        
        