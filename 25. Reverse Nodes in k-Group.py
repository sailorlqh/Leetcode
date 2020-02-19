# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def printnode(head):
            ans = []
            while(head != None):
                ans.append(head.val)
                head = head.next
            print(ans)
        def swap(head, k):
            newHead = head;
            curr = head;
            temp = head;
            for i in range(k - 1):
                temp = temp.next
                if(temp == None):
                    return head
            for i in range(k - 1):
                temp = curr.next.next
                temp1 = newHead
                newHead = curr.next
                newHead.next = temp1
                curr.next = temp
            return newHead
        if(k == 1):
            return head
        if(head == None):
            return None
        prev = ListNode(0)
        temp_head = prev
        temp_head.next = head
        curr = head
        flag = True
        while(flag):
            temp = curr
            for i in range(k-1):
                if(temp.next == None):
                    return temp_head.next
                temp = temp.next
            prev.next = swap(curr, k)
            for i in range(k-1):
                prev = prev.next
            if(curr.next != None):
                curr = curr.next
                prev = prev.next
            else:
                return temp_head.next
        