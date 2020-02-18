# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge2LinkedList(list1, list2):
            head = ListNode(-1)
            current = head
            while list1 != None and list2 != None:
                if(list1.val < list2.val):
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            if(list1 == None):
                current.next = list2
            else:
                current.next = list1
            return head.next
            
        length = len(lists)
        if(length == 0):
            return None
        if(length == 1):
            return lists[0]
        count = 1
        while(count < length):
            for i in range(0, length - count, count*2):
                print(i)
                lists[i] = merge2LinkedList(lists[i], lists[i + count])
            count *= 2
        return lists[0]
            
    
    
    
                
        