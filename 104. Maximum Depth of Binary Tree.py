class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, depth):
            if(node == None):
                return depth
            else:
                depth += 1
                return max(depth, helper(node.left, depth), helper(node.right, depth))
        return helper(root, 0)