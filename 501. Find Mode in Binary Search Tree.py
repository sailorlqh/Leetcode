# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        count = {}
        queue = []
        max_count = -1
        ans = []
        queue.append(root)
        while(root != None and len(queue) != 0):
            root = queue.pop(0)
            if(root.left != None):
                queue.append(root.left)
            if(root.right != None):
                queue.append(root.right)
            val = root.val
            if root.val in count.keys():
                count[val] += 1
            else:
                count[root.val] = 1
            if(count[val] > max_count):
                max_count = count[val]
                ans = [val]
            if(count[val] == max_count and val not in ans):
                ans.append(val)
        return ans
            
        