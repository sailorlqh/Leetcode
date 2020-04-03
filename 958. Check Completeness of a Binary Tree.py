class Solution:
    
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = []
        queue.append(root)
        flag = False
        while(queue):
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if(node == None):
                    flag = True
                    continue
                if(flag):
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True