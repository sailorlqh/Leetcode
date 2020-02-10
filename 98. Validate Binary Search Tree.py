# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        temp = -1000000000000
        if root == None:
            return True
        curr = root
        while(curr != None or len(stack) != 0):
            while(curr != None):
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if(curr.val <= temp):
                return False
            temp = curr.val
            curr = curr.right
        return True

            
        