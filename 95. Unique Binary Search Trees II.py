# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate(start, end):
            if(start > end):
                return [None]
            ans = []
            for i in range(start, end+1):
                left_sub_tree = generate(start, i-1)
                right_sub_tree = generate(i+1, end)
                
                for l in left_sub_tree:
                    for r in right_sub_tree:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
                        
        if(n == 0):
            return None
        else:
            return generate(1, n)
        