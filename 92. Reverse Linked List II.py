# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if head == None:
            return None
        current = head
        prev = None
        while m > 1:
            prev = current
            current = current.next
            m -= 1
            n -= 1
        temp = current
        temp1 = prev
        
        while n > 0:
            tempNode = current.next
            current.next = prev
            prev = current
            current = tempNode
            n -= 1
        if temp1 != None:
            temp1.next = prev
        else:
            head = prev
        temp.next = current
        return head
                