# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node1, node2):
            if(node1 == None and node2 == None):
                return True
            if(node1 == None or node2 == None):
                return False
            if(node1.val == node2.val):
                return helper(node1.left, node2.right) and helper(node1.right, node2.left)
            else:
                return False
            
        if(root == None):
            return True
        return helper(root, root)
        