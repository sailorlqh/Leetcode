#Since its a BST, root.val > left.val and root.val < right.val
#using inorder to travel through the tree, each time we pop somenode out
#those nodes form an increasing array
#therefore, we only need to compare the closest pair of nodes
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 100000
        curr_value = 100000
        stack = []
        while (root != None or len(stack) != 0):
            if(root != None):
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                temp = root.val
                ans = min(abs(curr_value - temp), ans)
                curr_value = temp
                root = root.right
        return ans