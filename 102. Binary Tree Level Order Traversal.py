# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root == None):
            return []
        res = []
        queue = []
        queue.append(root)
        temp = []
        while(len(queue) != 0):
            level = queue
            queue = []
            # queue.append([])
            for i in range(len(level)):
                temp.append(level[i].val)
                if(level[i].left != None):
                    queue.append(level[i].left)
                if(level[i].right != None):
                    queue.append(level[i].right)
            res.append(temp)
            temp = []
        return res
            
            
        
        