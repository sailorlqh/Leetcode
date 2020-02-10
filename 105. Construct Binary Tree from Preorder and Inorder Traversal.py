# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(a, b):
            length = len(a)
            if(length == 0):
                return None
            if(len(a) > 1):
                root = TreeNode(a[0])
                index = b.index(a[0])
                root.left = build(a[1:index + 1], b[0:index])
                root.right = build(a[index+1:], b[index+1:])
                return root
            else:
                return TreeNode(a[0])
            
        if(len(preorder) == 0):
            return None
        return build(preorder, inorder)
        
    
        

        

sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol.buildTree(preorder, inorder)
    
        