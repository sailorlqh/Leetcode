# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def helper(root):
            if(root != None):
                ans.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        return ans
        