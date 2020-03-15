# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        
        def traverse(root):
            if(root == None):
                return
            traverse(root.left)
            nodes.append(root)
            traverse(root.right)
            
        def balance(left, right):
            if(left > right):
                return None
            mid = (left + right) // 2
            root = nodes[mid]
            root.left = balance(left, mid-1)
            root.right = balance(mid+1, right)
            return root
        
        traverse(root)
        print(len(nodes))
        return balance(0, len(nodes) - 1)
        
        