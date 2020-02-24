# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(inorder_left, inorder_right, postorder_left, postorder_right):
        	if(inorder_left > inorder_right or postorder_left > postorder_right):
        		return None
        	root = TreeNode(postorder[postorder_right])
        	index = inorder.index(postorder[postorder_right])
        	root.left = helper(inorder_left,index-1, postorder_left,postorder_left + index - inorder_left - 1)
        	root.right = helper(index+1, inorder_right, postorder_left + index - inorder_left, postorder_right-1)
        	return root
        length = len(inorder)
        
        return helper(0,length-1, 0, length-1)

